import unittest

import eva_cttv_pipeline.trait_mapping.trait_names_parsing as trait_names_parsing


class TestGetTraitNames(unittest.TestCase):
    def test_get_trait_names_one(self):
        clinvar_json = {'clinvarSet': {'id': 14169895, 'title': 'NM_000285.3(PEPD):c.1153_1344del192 (p.Gly385_Gly448del) AND Prolidase deficiency', 'recordStatus': 'current', 'clinVarAssertion': [{'measureSet': {'measure': [{'measureRelationship': [{'symbol': [{'elementValue': {'value': 'PEPD', 'type': 'Preferred'}}], 'type': 'variant in gene'}], 'type': 'Variation', 'attributeSet': [{'attribute': {'value': 'EX14DEL', 'type': 'NonHGVS'}}], 'name': [{'elementValue': {'value': 'PEPD, EX14DEL', 'type': 'Preferred'}}], 'xref': [{'id': '613230.0002', 'db': 'OMIM', 'type': 'Allelic variant', 'status': 'CURRENT'}]}], 'type': 'Variant'}, 'id': 20377, 'clinVarAccession': {'orgID': 3, 'dateUpdated': 1475622000000, 'type': 'SCV', 'acc': 'SCV000020377', 'version': 1}, 'recordStatus': 'current', 'observedIn': [{'sample': {'species': {'value': 'human'}, 'origin': 'germline', 'affectedStatus': 'not provided'}, 'observedData': [{'citation': [{'id': [{'value': '1972707', 'source': 'PubMed'}]}, {'id': [{'value': '1688567', 'source': 'PubMed'}]}, {'id': [{'value': '2010534', 'source': 'PubMed'}]}], 'xref': [{'id': '170100', 'db': 'OMIM', 'type': 'MIM', 'status': 'CURRENT'}], 'attribute': {'value': "Tanoue et al. (1990) analyzed DNA from 3 patients with prolidase deficiency (170100) by Southern blot analysis after TaqI or BamHI digestion. A partial deletion of several hundred basepairs in the PEPD gene, which eliminated exon 14, was found in a patient and her affected sister, who were the offspring of a consanguineous mating (Endo et al., 1990). The defect appeared to be homozygous. No major abnormality in gene structure was found in 2 other patients. Tanoue et al. (1991) gave further details: the 774-bp deletion had termini within short, direct repeats. 'Slipped mispairing' was thought to have been involved in the generation of the deletion. The mutation caused a 192-bp in-frame deletion of prolidase mRNA. The parents were consanguineous. The oldest sister, 25 years of age at the time of report, developed skin lesions at the age of 19 months and required specific treatment. Her homozygous sister had no prominent changes in the skin until age 18 years. Both were negative for immunologic crossreacting material, and there was no residual activity of prolidase in the fibroblasts. Both excreted massive amounts of imidodipeptide in the urine. Erythrocyte prolidase activities were about 50% of the control value in the first-cousin parents.", 'type': 'Description'}}], 'method': [{'methodType': 'LITERATURE_ONLY'}]}], 'clinicalSignificance': {'reviewStatus': 'NO_ASSERTION_CRITERIA_PROVIDED', 'description': ['Pathogenic'], 'dateLastEvaluated': 670460400000}, 'externalID': {'id': '613230.0002', 'db': 'OMIM', 'type': 'Allelic variant', 'status': 'CURRENT'}, 'clinVarSubmissionID': {'localKey': '613230.0002_PROLIDASE DEFICIENCY', 'submitterDate': 1280444400000, 'title': 'PEPD, EX14DEL_PROLIDASE DEFICIENCY', 'submitter': 'OMIM'}, 'assertion': {'type': 'variation to disease'}, 'traitSet': {'trait': [{'type': 'Disease', 'name': [{'elementValue': {'value': 'PROLIDASE DEFICIENCY', 'type': 'Preferred'}}]}], 'type': 'Disease'}}], 'referenceClinVarAssertion': {'measureSet': {'id': 209, 'measure': [{'id': 15248, 'cytogeneticLocation': ['19cen-q13.11'], 'measureRelationship': [{'sequenceLocation': [{'displayStart': 33386949, 'accession': 'NC_000019.10', 'stop': 33521893, 'assembly': 'GRCh38', 'assemblyStatus': 'current', 'assemblyAccessionVersion': 'GCF_000001405.28', 'strand': '-', 'chr': '19', 'start': 33386949, 'displayStop': 33521893}, {'displayStart': 33877854, 'accession': 'NC_000019.9', 'stop': 34012798, 'assembly': 'GRCh37', 'assemblyStatus': 'previous', 'assemblyAccessionVersion': 'GCF_000001405.25', 'strand': '-', 'chr': '19', 'variantLength': 134945, 'start': 33877854, 'displayStop': 34012798}], 'symbol': [{'elementValue': {'value': 'PEPD', 'type': 'Preferred'}}], 'type': 'within single gene', 'name': [{'elementValue': {'value': 'peptidase D', 'type': 'Preferred'}}], 'xref': [{'id': '5184', 'db': 'Gene', 'status': 'CURRENT'}, {'id': '613230', 'db': 'OMIM', 'type': 'MIM', 'status': 'CURRENT'}, {'id': 'HGNC:8840', 'db': 'HGNC', 'status': 'CURRENT'}]}], 'name': [{'elementValue': {'value': 'NM_000285.3(PEPD):c.1153_1344del192 (p.Gly385_Gly448del)', 'type': 'Preferred'}}], 'xref': [{'id': 'nssv7487199', 'db': 'dbVar', 'status': 'CURRENT'}, {'id': 'nsv1197583', 'db': 'dbVar', 'status': 'CURRENT'}, {'id': '613230.0002', 'db': 'OMIM', 'type': 'Allelic variant', 'status': 'CURRENT'}], 'type': 'Deletion', 'attributeSet': [{'attribute': {'value': 'NM_000285.3:c.1153_1344del192', 'accession': 'NM_000285', 'change': 'c.1153_1344del192', 'type': 'HGVS, coding, RefSeq', 'version': 3}}, {'attribute': {'value': 'NG_013358.1:g.(138270_138276)_(139046_139051)del', 'accession': 'NG_013358', 'change': 'g.(138270_138276)_(139046_139051)del', 'type': 'HGVS, genomic, RefSeqGene', 'version': 1}}, {'attribute': {'accession': 'NC_000019', 'integerValue': 38, 'value': 'NC_000019.10:g.(33387843_33387848)_(33388618_33388624)del', 'type': 'HGVS, genomic, top level', 'change': 'g.(33387843_33387848)_(33388618_33388624)del', 'version': 10}}, {'xref': [{'id': '37', 'db': 'ClinVar', 'status': 'CURRENT'}], 'attribute': {'accession': 'NC_000019', 'integerValue': 37, 'value': 'NC_000019.9:g.(33878749_33878754)_(33879524_33879530)del', 'type': 'HGVS, genomic, top level, previous', 'change': 'g.(33878749_33878754)_(33879524_33879530)del', 'version': 9}}, {'attribute': {'value': 'NP_000276.2:p.Gly385_Gly448del', 'accession': 'NP_000276', 'change': 'p.Gly385_Gly448del', 'type': 'HGVS, protein, RefSeq', 'version': 2}}, {'xref': [{'id': '613230.0002', 'db': 'OMIM', 'type': 'Allelic variant', 'status': 'CURRENT'}], 'attribute': {'value': 'EX14DEL', 'type': 'nucleotide change'}}], 'comment': [{'value': 'NCBI staff reviewed the sequence information reported in PubMed 2010534 to determine the location of this deletion on the current reference sequence.', 'type': 'PUBLIC', 'dataSource': 'NCBI curation'}, {'value': '774-bp genomic deletion from PEPD, spanning exon 14 plus flanking intronic sequences.', 'type': 'PUBLIC', 'dataSource': 'NCBI curation'}, {'value': 'Genomic deletion from intron 13 to intron 14 results in skipping of exon 14.', 'type': 'LOCATION_ON_GENOME_AND_PRODUCT_NOT_ALIGNED', 'dataSource': 'NCBI curation'}], 'sequenceLocation': [{'displayStart': 33387843, 'strand': '-', 'assemblyStatus': 'current', 'chr': '19', 'innerStop': 33388618, 'outerStart': 33387843, 'accession': 'NC_000019.10', 'outerStop': 33388624, 'displayStop': 33388624, 'assemblyAccessionVersion': 'GCF_000001405.28', 'assembly': 'GRCh38', 'innerStart': 33387848}, {'displayStart': 33878749, 'assemblyStatus': 'previous', 'chr': '19', 'innerStop': 33879524, 'variantLength': 771, 'outerStart': 33878749, 'accession': 'NC_000019.9', 'outerStop': 33879530, 'displayStop': 33879530, 'assemblyAccessionVersion': 'GCF_000001405.25', 'assembly': 'GRCh37', 'innerStart': 33878754}]}], 'type': 'Variant', 'name': [{'elementValue': {'value': 'NM_000285.3(PEPD):c.1153_1344del192 (p.Gly385_Gly448del)', 'type': 'Preferred'}}]}, 'dateLastUpdated': 1475449200000, 'id': 57736, 'recordStatus': 'current', 'observedIn': [{'sample': {'species': {'value': 'human', 'taxonomyId': 9606}, 'origin': 'germline', 'affectedStatus': 'not provided'}, 'observedData': [{'id': 13597526, 'citation': [{'id': [{'value': '1688567', 'source': 'PubMed'}], 'type': 'general'}, {'id': [{'value': '1972707', 'source': 'PubMed'}], 'type': 'general'}, {'id': [{'value': '2010534', 'source': 'PubMed'}], 'type': 'general'}], 'attribute': {'value': "Tanoue et al. (1990) analyzed DNA from 3 patients with prolidase deficiency (170100) by Southern blot analysis after TaqI or BamHI digestion. A partial deletion of several hundred basepairs in the PEPD gene, which eliminated exon 14, was found in a patient and her affected sister, who were the offspring of a consanguineous mating (Endo et al., 1990). The defect appeared to be homozygous. No major abnormality in gene structure was found in 2 other patients. Tanoue et al. (1991) gave further details: the 774-bp deletion had termini within short, direct repeats. 'Slipped mispairing' was thought to have been involved in the generation of the deletion. The mutation caused a 192-bp in-frame deletion of prolidase mRNA. The parents were consanguineous. The oldest sister, 25 years of age at the time of report, developed skin lesions at the age of 19 months and required specific treatment. Her homozygous sister had no prominent changes in the skin until age 18 years. Both were negative for immunologic crossreacting material, and there was no residual activity of prolidase in the fibroblasts. Both excreted massive amounts of imidodipeptide in the urine. Erythrocyte prolidase activities were about 50% of the control value in the first-cousin parents.", 'type': 'Description'}}], 'method': [{'methodType': 'LITERATURE_ONLY'}]}], 'clinicalSignificance': {'reviewStatus': 'NO_ASSERTION_CRITERIA_PROVIDED', 'description': 'Pathogenic', 'dateLastEvaluated': 670460400000}, 'clinVarAccession': {'dateUpdated': 1475622000000, 'type': 'RCV', 'acc': 'RCV000000233', 'version': 2}, 'dateCreated': 1344812400000, 'assertion': {'type': 'VARIATION_TO_DISEASE'}, 'traitSet': {'id': 70, 'trait': [{'id': 3535, 'type': 'Disease', 'attributeSet': [{'attribute': {'value': 'Prolidase deficiency is characterized by skin lesions (typically severe, chronic, recalcitrant, and painful skin ulcers of the lower extremities and telangiectasias of the face and hands), recurrent infections (particularly of the skin and respiratory tract), dysmorphic facial features, variable intellectual disability, and hepatomegaly with elevated liver enzymes and splenomegaly. Anemia, thrombocytopenia, hypergammaglobulinemia, and hypocomplementemia are common. An association between systemic lupus erythematosus (SLE) and prolidase deficiency has been described.', 'type': 'public definition'}}, {'xref': [{'id': '742', 'db': 'Orphanet', 'status': 'CURRENT'}], 'attribute': {'value': 'Adult', 'type': 'age of onset'}}, {'attribute': {'value': 'prolidase_deficiency', 'type': 'MalaCard linkname'}}], 'name': [{'elementValue': {'value': 'Prolidase deficiency', 'type': 'Preferred'}, 'xref': [{'id': 'Prolidase+deficiency/5991', 'db': 'Genetic Alliance', 'status': 'CURRENT'}, {'id': '7473', 'db': 'Office of Rare Diseases', 'status': 'CURRENT'}]}, {'elementValue': {'value': 'Orphanet:742', 'type': 'EFO id'}}, {'elementValue': {'value': 'Prolidase deficiency', 'type': 'EFO name'}}, {'elementValue': {'value': 'http://www.orpha.net/ORDO/Orphanet_742', 'type': 'EFO URL'}}], 'xref': [{'id': 'C0268532', 'db': 'MedGen', 'status': 'CURRENT'}, {'id': '742', 'db': 'Orphanet', 'status': 'CURRENT'}, {'id': '170100', 'db': 'OMIM', 'type': 'MIM', 'status': 'CURRENT'}]}], 'type': 'Disease'}}}}

        expected_trait_names_list = ['prolidase deficiency']

        self.assertEqual(trait_names_parsing.get_trait_names(clinvar_json),
                         expected_trait_names_list)

    def test_get_trait_names_one(self):
        clinvar_json = {'clinvarSet': {'id': 14342293, 'title': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del AND multiple conditions', 'recordStatus': 'current', 'clinVarAssertion': [{'measureSet': {'measure': [{'type': 'Variation', 'attributeSet': [{'attribute': {'value': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del', 'type': 'HGVS'}}]}], 'type': 'Variant'}, 'id': 286587, 'clinVarAccession': {'orgID': 504935, 'dateUpdated': 1475622000000, 'type': 'SCV', 'acc': 'SCV000114929', 'version': 2}, 'recordStatus': 'current', 'observedIn': [{'sample': {'species': {'value': 'human', 'taxonomyId': 9606}, 'age': [{'value': 0, 'type': 'minimum', 'ageUnit': 'years'}, {'value': 9, 'type': 'maximum', 'ageUnit': 'years'}], 'gender': 'female', 'origin': 'germline', 'affectedStatus': 'yes', 'numberTested': 1, 'familyData': {'familyHistory': 'No'}}, 'observedData': [{'attribute': {'integerValue': 1, 'type': 'VariantAlleles'}}], 'method': [{'namePlatform': 'Oligo aCGH (V8.1)', 'methodType': 'CLINICAL_TESTING', 'purpose': 'discovery', 'typePlatform': 'microarray', 'description': 'Probe signal intensity'}]}], 'clinicalSignificance': {'reviewStatus': 'NO_ASSERTION_CRITERIA_PROVIDED', 'description': ['Pathogenic']}, 'clinVarSubmissionID': {'localKey': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del|Structural brain abnormalities|Neurological deficit', 'submitterDate': 1400108400000, 'submitter': 'Medical Genetics Laboratories, Baylor College of Medicine'}, 'assertion': {'type': 'variation to disease'}, 'traitSet': {'trait': [{'type': 'Disease', 'name': [{'elementValue': {'value': 'Structural brain abnormalities', 'type': 'Preferred'}}]}, {'type': 'Disease', 'name': [{'elementValue': {'value': 'Neurological deficit', 'type': 'Preferred'}}]}], 'type': 'Disease'}}], 'referenceClinVarAssertion': {'measureSet': {'id': 135643, 'measure': [{'id': 139361, 'type': 'Deletion', 'attributeSet': [{'attribute': {'accession': 'NC_000006', 'integerValue': 36, 'value': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del', 'type': 'HGVS, genomic, top level, previous', 'change': 'g.(159830469_159869956)_(170226118_170673013)del', 'version': 10}}], 'name': [{'elementValue': {'value': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del', 'type': 'Preferred'}}], 'sequenceLocation': [{'displayStart': 159830469, 'strand': '+', 'assemblyStatus': 'previous', 'innerStart': 159869956, 'innerStop': 170226118, 'variantLength': 10356163, 'outerStart': 159830469, 'accession': 'NC_000006.10', 'outerStop': 170673013, 'displayStop': 170673013, 'assemblyAccessionVersion': 'GCF_000001405.12', 'assembly': 'NCBI36', 'chr': '6'}]}], 'type': 'Variant', 'name': [{'elementValue': {'value': 'NC_000006.10:g.(159830469_159869956)_(170226118_170673013)del', 'type': 'Preferred'}}]}, 'dateLastUpdated': 1475449200000, 'id': 286871, 'recordStatus': 'current', 'observedIn': [{'sample': {'species': {'value': 'human', 'taxonomyId': 9606}, 'origin': 'germline', 'affectedStatus': 'yes'}, 'observedData': [{'id': 13710021, 'attribute': {'value': 'No', 'type': 'FamilyHistory'}}, {'id': 13710021, 'attribute': {'value': 'not provided', 'type': 'Description'}}], 'method': [{'namePlatform': 'Oligo aCGH (V8.1)', 'description': 'Probe signal intensity', 'purpose': 'Discovery', 'methodType': 'CLINICAL_TESTING'}]}], 'clinicalSignificance': {'reviewStatus': 'NO_ASSERTION_CRITERIA_PROVIDED', 'description': 'Pathogenic'}, 'clinVarAccession': {'dateUpdated': 1475622000000, 'type': 'RCV', 'acc': 'RCV000122722', 'version': 1}, 'dateCreated': 1402614000000, 'assertion': {'type': 'VARIATION_TO_DISEASE'}, 'traitSet': {'id': 14064, 'trait': [{'id': 19045, 'traitRelationship': [{'id': 70, 'type': 'co-occurring condition'}], 'type': 'Disease', 'name': [{'elementValue': {'value': 'Structural brain abnormalities', 'type': 'Preferred'}}], 'xref': [{'id': 'C1866933', 'db': 'MedGen', 'status': 'CURRENT'}]}, {'id': 19046, 'traitRelationship': [{'id': 70, 'type': 'co-occurring condition'}], 'type': 'Disease', 'name': [{'elementValue': {'value': 'Neurological deficit', 'type': 'Preferred'}}], 'xref': [{'id': 'C0521654', 'db': 'MedGen', 'status': 'CURRENT'}]}], 'type': 'Disease'}}}}

        expected_trait_names_list = ['structural brain abnormalities', 'neurological deficit']

        self.assertEqual(trait_names_parsing.get_trait_names(clinvar_json),
                         expected_trait_names_list)
