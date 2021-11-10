# Resources for technical standards, systems development, and interoperability

This resource serves as an entry point to topics related to standards and interoperability relevant to Pathology and Laboratory Medicine. It is not intended to be comprehensive. Instead, content here should highlight current and emerging topics likely to be of interest to the API community.

## Technical standards

### LOINC

- Main site at Regenstrief: https://loinc.org/

#### Automated LOINC mapping

A number of efforts to provide automated or semi-automated approaches to ensuring consistent selection of LOINC identifiers across organizations and data sets have been described.

- Parr, et al.[^parr_2018]

#### Criticisms of LOINC

Important criticisms regarding the real-world utility of LOINC have been raised. Some notable examples:

- Stram, et. al. (2020)[^stram-2020] described inconsistencies in the selection of LOINC identifiers for coagulation assays and cardiac markers in a large survey of laboratories.

### SNOMED
### HL7 2.x
### FHIR
### DICOM

## Subspecialty topics
### Genetics/Genomics
- The Association for Molecuar Pathology (AMP) released a statement titled [AMP Position Statement on Variant Data Sharing](https://www.amp.org/AMP/assets/File/advocacy/AMP_Position_Variant_Data_Sharing_7_29_2021.pdf) in July 2021 that explores challenges and barriers to sharing and representing genetic variants.
## Legislation and mandates
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

## References

[^parr_2018]: Parr SK, et al. Automated mapping of laboratory tests to LOINC codes using noisy labels in a national electronic health record system database. J Am Med Inform Assoc. 2018 [PMID 30137378](https://pubmed.ncbi.nlm.nih.gov/30137378/)
[^stram-2020]: Stram M, et al. A Survey of LOINC Code Selection Practices Among Participants of the College of American Pathologists Coagulation (CGL) and Cardiac Markers (CRT) Proficiency Testing Programs. Arch Pathol Lab Med. 2020 [PMID 31603714](https://pubmed.ncbi.nlm.nih.gov/31603714/)
