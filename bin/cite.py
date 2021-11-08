#!/usr/bin/env python3

"""Print a citation in markdown format given a pubmed ID

"""

import sys
import argparse
import json
from urllib.request import urlopen
from urllib.parse import urlencode


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('pmid', help="A PubMed ID")
    parser.add_argument('-o', '--outfile', help="Output file [default stdout]",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    params = urlencode({'db': 'pubmed', 'id': args.pmid, 'retmode': 'json'})
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?' + params
    with urlopen(url) as u:
        response = json.loads(u.read())

    try:
        result = response['result'][args.pmid]
    except KeyError:
        sys.exit(f'Could not retrieve PubMed ID "{args.pmid}"')

    pubyear = result['pubdate'].split()[0]
    author = result['authors'][0]['name']
    citelabel = '{}-{}'.format(author.split()[0].lower(), pubyear)

    markdown = ('[^{citelabel}]: {author}, et al. {title} {source}. '
                '{pubyear} [PMID {uid}](https://pubmed.ncbi.nlm.nih.gov/{uid}/)').format(
                    pubyear=pubyear, author=author, citelabel=citelabel, **result)

    args.outfile.write(markdown + '\n')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
