#!/usr/bin/env nextflow

nextflow.enable.dsl=2


def helpMessage() {
    log.info"""
    Generate automated trait mappings and table for manual curation.

    Params:
        --curation_root     Directory for current batch
        --clinvar           ClinVar XML file (optional, will download latest if omitted)
        --chunk_size        Chunk size to split traits into (default 1000)
        --max_forks         Max number of processes to run in parallel (default 10)
    """
}

params.help = null
params.curation_root = null
params.clinvar = null
params.chunk_size = 1000
params.max_forks = 10

if (params.help) {
    exit 0, helpMessage()
}
if (!params.curation_root) {
    exit 1, helpMessage()
}
curationRoot = params.curation_root


/*
 * Main workflow.
 */
workflow {
    if (params.clinvar != null) {
        clinvarXml = Channel.fromPath(params.clinvar)
    } else {
        clinvarXml = downloadClinvar()
    }

    parseTraits(clinvarXml)
    splitTraits(parseTraits.out.parsedTraits)
    processTraits(splitTraits.out.traitChunk.flatten())
    collectAutomatedMappings(processTraits.out.automatedTraits.collect())
    collectCurationTraits(processTraits.out.traitsForCuration.collect())
    createCurationTable(collectCurationTraits.out.curationTraits)
}

/*
 * Download ClinVar data, using the most recent XML dump.
 */
process downloadClinvar {
    output:
    path "clinvar.xml.gz", emit: clinvarXml

    script:
    """
    wget -O clinvar.xml.gz \
        https://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml/ClinVarFullRelease_00-latest.xml.gz
    """
}

/*
 * Parse traits from ClinVar XML.
 */
process parseTraits {
    input:
    path clinvarXml

    output:
    path "parsed_traits.csv", emit: parsedTraits

    script:
    """
    \${PYTHON_BIN} \${CODE_ROOT}/bin/trait_mapping/parse_traits.py \
        -i ${clinvarXml} \
        -o parsed_traits.csv
    """
}

/*
 * Split parsed traits into multiple chunks.
 */
process splitTraits {
    input:
    path parsedTraits

    output:
    path("parsed_traits-*", emit: traitChunk)

    script:
    """
    split -a 5 -d -l ${params.chunk_size} ${parsedTraits} parsed_traits-
    """
}

/*
 * Process traits through Zooma and OLS.
 */
process processTraits {
    maxForks params.max_forks
    errorStrategy 'finish'

    input:
    each path(traitChunk)

    output:
    path "automated_traits_*.tsv", emit: automatedTraits
    path "curation_traits_*.tsv", emit: traitsForCuration

    script:
    """
    \${PYTHON_BIN} \${CODE_ROOT}/bin/trait_mapping/process_traits.py \
        -i ${traitChunk} \
        -o automated_traits_${traitChunk}.tsv \
        -c curation_traits_${traitChunk}.tsv
    """
}

/*
 * Aggregate automated trait mappings into a single file.
 */
process collectAutomatedMappings {
    publishDir "${curationRoot}",
        overwrite: true,
        mode: "copy",
        pattern: "*.tsv"

    input:
    path "automated_traits_*.tsv"

    output:
    path "automated_trait_mappings.tsv", emit: automatedTraits

    script:
    """
    echo -e "#clinvar_trait_name\turi\tlabel" > automated_trait_mappings.tsv
    cat automated_traits_*.tsv >> automated_trait_mappings.tsv
    """
}

/*
 * Aggregate traits for manual curation into a single file.
 */
process collectCurationTraits {
    input:
    path "curation_traits_*.tsv"

    output:
    path "traits_requiring_curation.tsv", emit: curationTraits

    script:
    """
    cat *.tsv > traits_requiring_curation.tsv
    """
}

/*
 * Create the table for manual curation.
 */
process createCurationTable {
    publishDir "${curationRoot}",
        overwrite: true,
        mode: "copy",
        pattern: "*.tsv"

    input:
    path curationTraits

    output:
    path "google_sheets_table.tsv", emit: curationTable

    script:
    """
    \${PYTHON_BIN} \${CODE_ROOT}/bin/trait_mapping/create_table_for_manual_curation.py \
        --traits-for-curation ${curationTraits} \
        --previous-mappings \${BATCH_ROOT_BASE}/manual_curation/latest_mappings.tsv \
        --previous-comments \${BATCH_ROOT_BASE}/manual_curation/latest_comments.tsv \
        --output google_sheets_table.tsv
    """
}
