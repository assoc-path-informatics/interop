Title: Response to ONC Survey on 2030 Interoperability Goals
Slug: onc-survey
Date: 2021-11-12
Category: Policy
Tags: ONC

ONC is [soliciting input](https://www.healthit.gov/topic/interoperability/health-interoperability-outcomes-2030) for its Health Interoperability Outcomes 2030 initiative (more information [here](https://www.healthit.gov/buzz-blog/interoperability/health-interoperability-outcomes-2030)). The question posed by the ONC survey was shared on the API mailing list, and responses from the API membership are summarized here. API encourages the pathology informatics community to submit responses to the survey. Everyone should feel free to use the list below as a source of ideas, or even to submit items verbatim.

## List of suggested goals/outcomes:
### Because of interoperability, before/by 2030 ...
* … healthcare providers will be able to order a laboratory test from any laboratory using the same test name.
* … pathologists will guide therapeutic management choices same day, not a day or weekend later.
* … there's a robust marketplace of medical software applications, breaking the Epic/Cerner oligopoly, so that clinicians and their institutions can choose from a wide range of highly usable apps that use patient-derived data to make it easier and more efficient to care for patients in high quality ways.
* … laboratory results will be able to be shared in a manner that uniquely identifies the method, device, and laboratory that produced it, including whether the result is traceable to an international reference material.
* … laboratory reporting for notifiable diseases will be entirely electronic at the national, state, and local level.
* … all data elements in a pathologist's synoptic cancer report will be available as for downstream use by EHRs and cancer registries as discrete, machine-readable, and SNOMED-encoded elements.
* … a patient will be able to send a DICOM file (or something else??) of their digital pathology images to any hospital in the United States and that hospital's pathologist will be able to review the images.
* … telepathology for either primary diagnosis or for expert consultation in difficult cases will become routine.
* …  a patient getting laboratory testing will be able to query their insurance provider and get a reasonable estimate of the cost to them of this testing.
* … there will be large-scale monitoring of commercial assay results by test kit and reagent/calibrator lot such that real lot-lot variability is known by vendor. New lots with problems are recognized by result median and distribution shifts less than a week after deployment, and fixes are verified in a similar time frame.
* … many more tests will produce results that are traceable to standardized reference materials and reference methods. The data model for tests will include traceability. Results from tests that are standardized in the same way can be displayed and trended together across provider organizations, and processed by the same decision support rules and machine learning models.
* … there will be new patient-centric data standards (eg. standard universal patient ID).
* … pagers are no longer used as a primary means of inter-hospital communication by 2030.
* … health IT platforms will be designed primarily for communication and collaboration. Business transactions and compliance functionality will be secondary rather than central functions.
* … patient data will become portable in a secure manner.
* … will be established seamless data querying mechanisms for public health actions.
* … will be established real time big data research tools on a national/international level while protecting individual privacy and security.
* … there is a robust coding system we would commit to using and which fields in HL7 should be used and populated to make pathology/lab-medicine data as specific as possible and standardized as much as possible.
* … the lab interoperability nuances are well articulated and understood on all levels.
* … we have a clear definition of interoperability and clear understanding of the goals and priorities of lab interoperability

* … all stakeholders of interoperability are identified with clearly stated interests in lab interoperability. (e.g. regulatory agencies (ONC, FDA, CMS), diagnostic device/kit vendors, laboratorians, clinicians, and public health and health services researchers). The superset of the partially overlapping goals of these individual constituencies is identified
* … there is a comprehensive statement of the interoperability requirements.
* … there are relevant examples of interoperability in pathology that illustrate successes and challenges.

* … data model for lab tests is well defined by domain experts and includes all elements that are needed for clearly defined use cases or workflow scenarios.

* … it will become clear that existing standards are not adequate (not by a long shot) for common laboratory tests and are unusable for more complicated tests such as pathology and genomic reports.
* … there will be one interoperability standard because there is significant cross-over between pathology, genomics and clinical laboratory tests (e.g., cultures on tissue also examined for pathology).
* … the standards will be accessed for their safety when used for interoperability. (Ease of data retrieval differs from interoperability safety).
The scenarios below illustrate that seemingly interoperable terminology, semantically similar, may lack the depth of meaning for a particular activity in the context of direct patient care as opposed to data aggregation and analysis where it would be perfectly adequate:
  1. Coding a laboratory test for data retrieval has far lower safety implications than putting a code on a test so that it can be automatically charted in a different EHR.
  1.	Miscoding a test is annoying for data retrieval and frankly dangerous for interoperability and patient care.
  1. Using a more generic code for a test may cause it to lose meaning such that misinterpretation is likely when the result is charted under a more generic name.
  1. Requiring 30+ codes for a single genomic variant is a maintenance nightmare and at high risk for error and misinterpretation when it is separated from the interpretation.
