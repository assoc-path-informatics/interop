import glob
from pathlib import Path

from pelican.settings import DEFAULT_CONFIG
from pelican.readers import MarkdownReader

config = DEFAULT_CONFIG.copy()

AUTHOR = 'Association for Pathology Informatics'
SITENAME = 'API Interoperability Resources'
SITEURL = 'https://assoc-path-informatics.github.io/interop'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "./elegant"

# place files replacing theme templates in ./content/templates
THEME_TEMPLATES_OVERRIDES = ['./content/templates']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

# prevent Pelican from reading files in the following directories
IGNORE_FILES = ['.#*', 'includes', 'templates']

# render markdown contents from files in /content/includes and make
# accesible from INCLUDES variable in html templates
INCLUDES = {}
for fname in glob.glob('./content/includes/*.md'):
    pth = Path(fname)
    INCLUDES[pth.stem], _ = MarkdownReader(config).read(fname)
