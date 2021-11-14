Title: About

This site is maintained by the [Association for Pathology
Informatics](https://pathologyinformatics.org) as a project of the
Technical Standards Committee.

## contributing

- Source code for this site is hosted on GitHub: <https://github.com/assoc-path-informatics/interop>.
- Those who are comfortable with git are encouraged to submit pull requests from a fork of this repository. See the repository for details, but in a nutshell: each page corresponds to a Markdown file in the ``/content`` directory (<https://github.com/assoc-path-informatics/interop/tree/main/content>). The site is rebuilt using a GitHub action each time a change is pushed to the ``main`` branch.
- Others: your input is welcome! If possible, please use [GitHub Issues](https://github.com/assoc-path-informatics/interop/issues) to submit comments, corrections, and additions. Otherwise please email one of the authors listed on the site or the API mailing list.

## style guide

- This document is composed in Markdown format as implemented by [Python-Markdown](https://python-markdown.github.io).
- Urls less than 40 characters or so should be displayed inline so that the hostname and full path is visible (eg, formatted with angle braces like ``<https://example.com>``); longer urls should be presented as a hyperlink using [Markdown syntax](https://github.github.com/gfm/#links), eg ``[example link](https://example.com)``.
- Please include pubmed citations as footnotes (see examples below). The python script [bin/cite.py](https://github.com/assoc-path-informatics/interop/blob/main/bin/cite.py) can be used to format citations given a PMID. Citations may also be formatted manually.

## software

This site uses [Pelican](https://blog.getpelican.com) with the
[Elegant](https://github.com/Pelican-Elegant/elegant) theme and is
hosted on GitHub pages.
