# Topics related to Laboratory data interoperability.

Source code for <https://assoc-path-informatics.github.io/interop>, a
website maintained by the [Association for Pathology Informatics](https://pathologyinformatics.org).

[![Pelican site CI](https://github.com/assoc-path-informatics/interop/actions/workflows/pelican.yml/badge.svg)](https://github.com/assoc-path-informatics/interop/actions/workflows/pelican.yml)

## Adding entries

Entries are created by adding Markdown files to the
[/content](/content) directory. Note that users with permission to
commit to this repository can edit or add pages directly from GitHub
using the web editor. See the "Add file" option at the top right of
the file listing or view a file and choose the pencil
option. Additional instructions and guidelines can be found
[here](https://assoc-path-informatics.github.io/interop/pages/about.html).

The [Pelican documentation](https://docs.getpelican.com/en/latest/content.html#file-metadata)
describes how to specify metadata. For example:

```
Title: My super title
Slug: my-super-post
Date: 2010-12-03
Modified: 2010-12-05
Category: Python
Tags: pelican, publishing
Authors: Alexis Metaireau, Conan Doyle
```

Please include Title, Date, and Tags; others are optional (posts will
be added the "Misc" category be default).

Posts with ``Status: draft`` in the file metadata are not published (you can use
use this as a mechanism for hiding in-progress work).

By default urls are constructed from page titles, and it is useful to
include "Slug" for entries with long titles.

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

## Website deployment

This site is automatically rebuilt and deployed whenever a change is
pushed to the ``main`` branch. The status of each build action can be
viewed using the
[GitHub Actions console](https://github.com/assoc-path-informatics/interop/actions).

## Local development

It is not necessary to create a local development environment: content
may be added by simply editing files in ``/content`` and pushing the
changes. However, it may be useful to preview changes locally.

If desired, a local development environment can be created as follows. First,
clone this repository and enter the ``interop`` directory. The Elegant
theme is provided as a git submodule; this must be initiated the first
time the repo is cloned.

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

Now the website may be generated locally. By default, internal urls
contain the full path to the site hosted on GitHub pages, but it is
possible to use relative urls so that the site can be navigated
locally.

```
make html PELICANOPTS='-e RELATIVE_URLS=True'
```

View the website by launching a local webserver and visiting <https://localhost:8000>:

```
pelican --listen
```

If you are making many changes, it is convenient to use
``bin/watch.sh`` to both launch the Pelican server and rebuild the
site whenever a file is changed.
