Title: Genomics
Date: 2021-11-12
Category:
Tags: FHIR, ONC, GACS

- FHIR guidance for genomics data: <https://www.hl7.org/fhir/genomics.html>
- Dolin et al (2021)[^dolin-2021] describes a utility for converting variant data in VCF format into FHIR.
- Swaminathan R, et al.[^swaminathan-2016] compares the capabilities of the SMART Genomics API,  Google Genomics, and the 23andMe API.
- The Association for Molecuar Pathology (AMP) released a statement titled [AMP Position Statement on Variant Data Sharing](https://www.amp.org/AMP/assets/File/advocacy/AMP_Position_Variant_Data_Sharing_7_29_2021.pdf) in July 2021 that explores challenges and barriers to sharing and representing genetic variants.

# ONC "Sync for genes"

In 2017 ONC published a [report](https://www.healthit.gov/sites/default/files/sync_for_genes_report_november_2017.pdf) titled *Sync for Genes: enabling clinical genomics for precision medicine via HL7® fast healthcare interoperability resources.* This document outlines proposed recommendations for a national standard for exchanging genomic data in response to [recommendations](https://www.healthit.gov/sites/default/files/facas/PMTF_Transmittal_Letter_2015-09-25_v2.pdf) from the Precision Medicine Task Force.

> Sync for Genes addresses a selection of the proposed items raised by the Task Force. Sync for Genes supports the ONC, NIH, and the Food and Drug Administration (FDA) toward fulfilling the Task Force’s recommendation to “[i]dentify opportunities for ONC to support our federal partners’ PMI efforts and related health IT/interoperability challenges, including National Cancer Institute, Food and Drug Administration, National Institutes of Health, and Department of Veterans Affairs.” Sync for Genes seeks to fulfill another recommendation — to “[i]dentify opportunities for ONC to collaborate with industry and pilot the use of standards to enable data donation and patient access through application programming interfaces (APIs) using standards such as FHIR and OAuth 2.0” — by utilizing FHIR Genomics and its leveraging of the SMART on FHIR Genomics framework as well as using the underlying security/privacy framework common to SMART on FHIR.

Notable discussion points include:

- Emphasis on an interoperability standard based on FHIR.
- Introduction of the concept of a Genomic Archive and Computer/Communication System (GACS): "A GACS acts in the same manner as a PACS — to store big data that is not suitable to store directly in an EHR."
- Presentation of a "list of the seven developed guidelines on standard development for enabling clinical genomics at point of care and facilitating precision medicine."
- Description of several Sync for Genes pilot projects using FHIR Genomics.

[^dolin-2021]: Dolin RH, et al. vcf2fhir: a utility to convert VCF files into HL7 FHIR format for genomics-EHR integration. BMC Bioinformatics. 2021 [PMID 33653260](https://pubmed.ncbi.nlm.nih.gov/33653260/)
[^swaminathan-2016]: Swaminathan R, et al. A Review on Genomics APIs. Comput Struct Biotechnol J. 2016 [PMID 26702340](https://pubmed.ncbi.nlm.nih.gov/26702340/)
