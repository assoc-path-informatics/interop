# Resources for technical standards, systems development, and interoperability

This resource serves as an entry point to topics related to standards and interoperability relevant to Pathology and Laboratory Medicine. It is not intended to be comprehensive. Instead, content here should highlight current and emerging topics likely to be of interest to the API community.

## Technical standards

### LOINC

- Main site at Regenstrief: https://loinc.org/

#### Automated LOINC mapping

A number of efforts to provide automated or semi-automated approaches to ensuring consistent selection of LOINC identifiers across organizations and data sets have been described.

- Parr, et al. (2018) [^parr_2018] describes "an automated machine learning pipeline that leverages noisy labels to map laboratory data to LOINC codes" using lab results in the VA data warehouse.

#### Criticisms of LOINC

Important criticisms regarding the real-world utility of LOINC have been raised. Some notable examples:

- Stram, et. al. (2020)[^stram-2020] described inconsistencies in the selection of LOINC identifiers for coagulation assays and cardiac markers in a large survey of laboratories.

### SNOMED
- Cancer Content to be used in eCCs
- Ongoing work to develop molecular concepts, eCC data field codes, and integration/coordination with LOINC for coverage of lab medicine concepts

### HL7 2.x

#### Specification Name
- Overview/purpose
- Standards Process Maturity
- Implementation Maturity
- Adoption Level
- Federally required (yes/no, details)
- Test tool availability

#### HL7 Version 2.5.1 Implementation Guide: Laboratory Orders from EHR (LOI), Release 1, STU Release 3  - US Realm
- Overview/purpose
- Standards Process Maturity
- Implementation Maturity
- Adoption Level
- Federally required (yes/no, details)
- Test tool availability
- https://www.hl7.org/implement/standards/product_brief.cfm?product_id=152

#### HL7 Version 2.5.1 Implementation Guide: Laboratory Results Interface, Release 1 STU Release 3 - US Realm
- This guide provides guidance on how to communicate laboratory results in general from a (reference) Laboratory’s LIS to a system interested in lab results, e.g., EHR, Public Health, other Laboratory.  It covers general lab results, as well as specifications focused on microbiology, newborn dried bloodspot screening, and clinical genomics.
- Standards Process Maturity
- Implementation Maturity
- Adoption Level
- Federally required (yes/no, details)
- Test tool availability
- https://www.hl7.org/implement/standards/product_brief.cfm?product_id=279

#### North American Association of Central Cancer Registries (NAACCR) Standards for Cancer Registries Volume V: Pathology Laboratory Electronic Reporting, Version 5.0
- The goal of this document is to define data standards and guidelines to transmit cancer information from laboratories to cancer registries. It also provides guidelines for the implementation of these standards by pathology laboratories, vendors, and other groups. 
- Standards Process Maturity
- Implementation Maturity
- Adoption Level
- Federally required (yes/no, details)
- Test tool availability
- https://www.naaccr.org/pathology-laboratory-electronic-reporting/

### FHIR
- LIVD
- Order Catalog IG, FHIR version of V2's eDOS
- General FHIR R5 enhancements
- Cancer Pathology Data Sharing
- IHE SDC on FHIR
- Genomics Reporting IG

### DICOM
- Working Group 26 https://www.dicomstandard.org/activity/wgs/wg-26

### Integrating the Healthcare Enterprise (IHE) Pathology and Laboratory Medicine (PaLM)
- Brief discussion of IHE interoperability profiles:
- LAW
- LCC
- DPIA
- LBL
- LTW
- LCSD
- LDA
- LPOCT

### CLSI
- AUTO15
- AUTO16

## Subspecialty topics
### Genetics/Genomics
- FHIR guidance for genomics data: https://www.hl7.org/fhir/genomics.html
- Dolin et al (2021)[^dolin-2021] describes a utility for converting variant data in VCF format into FHIR.
- The Association for Molecuar Pathology (AMP) released a statement titled [AMP Position Statement on Variant Data Sharing](https://www.amp.org/AMP/assets/File/advocacy/AMP_Position_Variant_Data_Sharing_7_29_2021.pdf) in July 2021 that explores challenges and barriers to sharing and representing genetic variants.
## Legislation and mandates

### ONC
 - ISA
 
 #### ONC Cures Act Final Rule:
 - Information Blocking
 - Certification
 - APIs
 - USCDI/USCDI+
 - SVAP
 - Enforcement discretion dates and timeframes
 - Text: https://www.federalregister.gov/documents/2020/05/01/2020-07419/21st-century-cures-act-interoperability-information-blocking-and-the-onc-health-it-certification

### CMS
 - MIPS/QPP/PIP as the mechanism by which CEHRT becomes required
 - Brief discussion of pathologist exemption in PIP

## Vendors and products

## Secure system and software development

## Maintaining this document

- This document is composed using GitHub Flavored Markdown: https://github.github.com/gfm/
- Urls less then 40 characters or so should be displayed inline so that the hostname and full path is visible (eg, see the link to the GFM spec above); longer urls should be presented as a hyperlink using [Markdown syntax](https://github.github.com/gfm/#links).
- Please include pubmed citations as footnotes (see examples below). The python script [bin/cite.py](bin/cite.py) can be used to format citations given a PMID. Citations may also be formatted manually.
- Maintainers: please make frequent, logical commits to facilitate the review process.
- Those who are comfortable with git are encouraged to submit pull requests from a fork of this repository.
- Others: your input is welcome! If possible, please use [GitHub Issues](https://github.com/assoc-path-informatics/interop/issues) to submit comments, corrections, and additions. Otherwise please email one of the maintainers listed below.

### Maintainers

- Peter Gershkovich, Yale University
- Noah Hoffman, University of Washington

### Contributors

- Alex Mays, Massachusetts General Hospital

## References

[^dolin-2021]: Dolin RH, et al. vcf2fhir: a utility to convert VCF files into HL7 FHIR format for genomics-EHR integration. BMC Bioinformatics. 2021 [PMID 33653260](https://pubmed.ncbi.nlm.nih.gov/33653260/)
[^parr_2018]: Parr SK, et al. Automated mapping of laboratory tests to LOINC codes using noisy labels in a national electronic health record system database. J Am Med Inform Assoc. 2018 [PMID 30137378](https://pubmed.ncbi.nlm.nih.gov/30137378/)
[^stram-2020]: Stram M, et al. A Survey of LOINC Code Selection Practices Among Participants of the College of American Pathologists Coagulation (CGL) and Cardiac Markers (CRT) Proficiency Testing Programs. Arch Pathol Lab Med. 2020 [PMID 31603714](https://pubmed.ncbi.nlm.nih.gov/31603714/)
