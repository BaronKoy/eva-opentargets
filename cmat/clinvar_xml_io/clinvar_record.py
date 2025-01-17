import logging
import re
import xml.etree.ElementTree as ElementTree
from xml.dom import minidom

from cmat.clinvar_xml_io.clinvar_measure import ClinVarRecordMeasure
from cmat.clinvar_xml_io.clinvar_trait import ClinVarTrait
from cmat.clinvar_xml_io.xml_parsing import find_elements, find_optional_unique_element, \
    find_mandatory_unique_element

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ClinVarRecord:
    """Instances of this class hold data on individual ClinVar records. See also:
    * /data-exploration/clinvar-variant-types/README.md for the in-depth explanation of ClinVar data model;
    * Issue https://github.com/EBIvariation/eva-opentargets/issues/127 for the most recent discussions on changing
      support of different ClinVar record types."""

    # A score for the review status of the assigned clinical significance ranges from 0 to 4 and corresponds to the
    # number of "gold stars" displayed on ClinVar website. See details here:
    # https://www.ncbi.nlm.nih.gov/clinvar/docs/details/#review_status
    score_map = {
        "no assertion provided": 0,
        'no assertion criteria provided': 0,
        'criteria provided, single submitter': 1,
        'criteria provided, conflicting interpretations': 1,
        'criteria provided, multiple submitters, no conflicts': 2,
        'reviewed by expert panel': 3,
        'practice guideline': 4,
    }

    # Some allele origin terms in ClinVar are essentially conveying lack of information and are thus not useful.
    NONSPECIFIC_ALLELE_ORIGINS = {'unknown', 'not provided', 'not applicable', 'tested-inconclusive', 'not-reported'}

    def __init__(self, rcv, trait_class=ClinVarTrait, measure_class=ClinVarRecordMeasure):
        """Initialise a ClinVar record object from an RCV XML record."""
        self.rcv = rcv

        # Add a list of traits
        self.trait_set = []
        for trait in find_elements(self.rcv, './TraitSet/Trait'):
            self.trait_set.append(trait_class(trait, self))

        # We are currently only processing MeasureSets of type Variant which are included directly in the RCV record.
        # Some other options (currently not supported) are:
        # * MeasureSet of types "Haplotype", "Phase unknown", or "Distinct chromosomes"
        # * GenotypeSet, which contains an assertion about a group of variants from different chromosome copies, with
        #   the type of be either a "CompoundHeterozygote" or a "Diplotype"
        variant_measure = find_optional_unique_element(self.rcv, './MeasureSet[@Type="Variant"]/Measure')
        if not variant_measure:
            self.measure = None
        else:
            self.measure = measure_class(variant_measure, self)

    def __str__(self):
        return f'ClinVarRecord object with accession {self.accession}'

    def write(self, output):
        xml_str = minidom.parseString(ElementTree.tostring(self.rcv)).toprettyxml(indent='  ', encoding='utf-8')
        # version 3.8 adds superfluous root
        if xml_str.startswith(b'<?xml'):
            xml_str = re.sub(b'<\?xml.*?>', b'', xml_str)
        xml_str = b'  '.join([s for s in xml_str.strip().splitlines(True) if s.strip()])
        xml_str += b'\n'
        output.write(xml_str)

    @property
    def accession(self):
        return find_mandatory_unique_element(self.rcv, './ClinVarAccession').attrib['Acc']

    @property
    def date(self):
        """This tracks the latest update date, counting even minor technical updates."""
        return self.rcv.attrib['DateLastUpdated']

    @property
    def last_evaluated_date(self):
        """This tracks the latest (re)evaluation date for the clinical interpretation.
        See https://github.com/opentargets/platform/issues/1161#issuecomment-683938510 for details."""
        # The DateLastEvaluated attribute is not always present. In this case, this property will be None.
        return find_mandatory_unique_element(self.rcv, './ClinicalSignificance').attrib.get('DateLastEvaluated')

    @property
    def review_status(self):
        """Return a review status text for the assigned clinical significance. See score_map above for the list of
        possible values."""
        review_status = find_mandatory_unique_element(self.rcv, './ClinicalSignificance/ReviewStatus').text
        assert review_status in self.score_map, f'Unknown review status {review_status} in RCV {self.accession}'
        return review_status

    @property
    def score(self):
        """Return a score (star rating) for the assigned clinical significance. See score_map above."""
        return self.score_map[self.review_status]

    @property
    def mode_of_inheritance(self):
        """Return a (possibly empty) list of modes of inheritance for a given ClinVar record."""
        return sorted({
            elem.text for elem in find_elements(self.rcv, './AttributeSet/Attribute[@Type="ModeOfInheritance"]')
        })

    @property
    def trait_set_type(self):
        return find_mandatory_unique_element(self.rcv, './TraitSet').attrib['Type']

    @property
    def traits(self):
        """Returns a list of traits associated with the ClinVar record, in the form of Trait objects."""
        return self.trait_set

    @property
    def traits_with_valid_names(self):
        """Returns a list of traits which have at least one valid (potentially resolvable) name."""
        return [trait for trait in self.trait_set if trait.preferred_or_other_valid_name]

    @property
    def evidence_support_pubmed_refs(self):
        """The references of this type represent evidence support for this specific variant being observed in this
        specific disease. These are the references displayed on the ClinVar website in the "Assertion and evidence
        details" section at the bottom of the page."""
        return [int(elem.text)
                for elem in find_elements(self.rcv, './ObservedIn/ObservedData/Citation/ID[@Source="PubMed"]')]

    @property
    def clinical_significance_raw(self):
        """The original clinical significance string as stored in ClinVar. Example: 'Benign/Likely benign'."""
        return find_mandatory_unique_element(self.rcv, './ClinicalSignificance/Description').text

    @property
    def clinical_significance_list(self):
        """The normalised deduplicated list of all clinical significance values. The original value is (1) split into
        multiple values by 3 delimiters: ('/', ', ', '; '), (2) converted into lowercase and (3) sorted
        lexicographically. Example: 'Benign/Likely benign, risk_factor' → ['benign', 'likely benign', 'risk factor'].
        See /data-exploration/clinvar-variant-types/README.md for further explanation."""
        return sorted(list(set(re.split('/|, |; ', self.clinical_significance_raw.lower().replace('_', ' ')))))

    @property
    def allele_origins(self):
        return {elem.text for elem in find_elements(self.rcv, './ObservedIn/Sample/Origin')}

    @property
    def valid_allele_origins(self):
        """Returns all valid allele origins, i.e. ones that are not in the list of nonspecific terms."""
        return {origin for origin in self.allele_origins if origin.lower() not in self.NONSPECIFIC_ALLELE_ORIGINS}
