# interop

Topics related to Laboratory data interoperability

## Adding entries

Entries are created by adding Markdown files to ``/content``. The
[Pelican documentation
](https://docs.getpelican.com/en/latest/content.html#file-metadata)
describes how to specify metadata. For example:

```
Title: My super title
Date: 2010-12-03
Modified: 2010-12-05
Category: Python
Tags: pelican, publishing
Authors: Alexis Metaireau, Conan Doyle
```

Please include Title, Date, Category, and Tags; others are optional.

Categories may be *one* of

- Vocabularies
- Formats
- Policy
- Legislation

A post may have more than one tag. Choose from the following:

- HL7
- LOINC
- SNOMED
- FHIR
- DICOM
- ...

The remainder of the post can contain arbitrary Markdown-formatted content.

## Local development

A local development environment can be created as follows. First,
clone this repository and enter repo directory. The Elegant theme is
provided as a git submodule; this must be initiated the first time the
repo is cloned.

```
git submodule init
git submodule update
```

Next, create a python virtualenv and install pelican.

```
python3 -m venv py3-env
source py3-env/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
```
