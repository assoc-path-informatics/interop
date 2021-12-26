Title: About

This site is maintained by the [Association for Pathology
Informatics](https://pathologyinformatics.org) as a project of the
Technical Standards Committee.

# purpose

The Technical Standards and Interoperability resources are created to express, discuss, and illustrate pressing issues of information exchange between clinical systems used in Pathology.
Digitized slides, AI algorithms, Data Exchange Interfaces, Dashboards and other types of visualization, workflow management systems in general greatly speed up the processing of data.
Converting data into information and assembling it at decision points to serve purposeful ends remains a challenge.

The API membership includes domain experts, users, and students of the standards and formats that enable interoperability between systems, and this project is intended to provide a convenient place to aggregate and summarize information relevant in the domain of laboratory and pathology informatics. A wealth of information exists online and in the literature, but it can be challenging to identify the most relevant and current resources.

# content and structure

This site is organized into posts or articles that explore aspects of interoperability. "Tags" can be used to identify specific standards or concepts addressed in each.

Contributions to this site can include any of the following:

- Links to online resources.
- Citations of notable reviews, studies, or opinion pieces in the literature.
- Brief summaries of individual topics.

# contributing

- Source code for this site is hosted on [GitHub](https://github.com/assoc-path-informatics/interop/tree/main/content).
- See the repository for details, but in a nutshell: each page corresponds to a Markdown file in the [content](https://github.com/assoc-path-informatics/interop/tree/main/content) directory of the repository. The site is rebuilt using a GitHub action each time a change is pushed to the ``main`` branch.
- Those who are comfortable with git are encouraged to submit pull requests from a fork of this repository.
- Others: your input is welcome! If possible, please use [GitHub Issues](https://github.com/assoc-path-informatics/interop/issues) to submit ideas, comments, corrections, and additions (requires a free GitHub account). We will also use GitHub issues to discuss topics and develop content. Otherwise please email one of the authors listed on the site or the API mailing list.
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
- When updating an existing page, please indicate the date of modification in the header by adding ``Modified: YYYY-MM-DD``.
- Please include pubmed citations as footnotes (see examples in existing articles). The python script [bin/cite.py](https://github.com/assoc-path-informatics/interop/blob/main/bin/cite.py) can be used to format citations given a PMID. Citations may also be formatted manually.

# software

This site uses [Pelican](https://blog.getpelican.com) with the
[Flex](https://github.com/alexandrevicenzi/Flex) theme and is
hosted on GitHub pages.
