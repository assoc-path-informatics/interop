Title: About

This site is maintained by the [Association for Pathology
Informatics](https://pathologyinformatics.org) as a project of the
Technical Standards Committee.

# contributing

- Source code for this site is hosted on [GitHub](https://github.com/assoc-path-informatics/interop/tree/main/content).
- See the repository for details, but in a nutshell: each page corresponds to a Markdown file in the [content](https://github.com/assoc-path-informatics/interop/tree/main/content) directory of the repository. The site is rebuilt using a GitHub action each time a change is pushed to the ``main`` branch.
- Those who are comfortable with git are encouraged to submit pull requests from a fork of this repository.
- Others: your input is welcome! If possible, please use [GitHub Issues](https://github.com/assoc-path-informatics/interop/issues) to submit comments, corrections, and additions (requires a free GitHub account). Otherwise please email one of the authors listed on the site or the API mailing list.
- Regular contributors can be granted access to make changes to the repository directory.

# style guide

- This document is composed in Markdown format. Here's a [cheat sheet](https://www.markdownguide.org/cheat-sheet/) describing the basics. [Here](https://raw.githubusercontent.com/assoc-path-informatics/interop/main/content/pages/about.md) is the source code for this page!
- Urls less than 40 characters or so should be displayed inline so that the hostname and full path is visible (eg, formatted with angle braces) like this:
```
<https://example.com>
```
- Longer urls should be presented as a hyperlink using [Markdown syntax](https://github.github.com/gfm/#links), e.g.
```
[example link](https://example.com)
```
- Please include pubmed citations as footnotes (see examples in existing articles). The python script [bin/cite.py](https://github.com/assoc-path-informatics/interop/blob/main/bin/cite.py) can be used to format citations given a PMID. Citations may also be formatted manually.

# software

This site uses [Pelican](https://blog.getpelican.com) with the
[Elegant](https://github.com/Pelican-Elegant/elegant) theme and is
hosted on GitHub pages.
