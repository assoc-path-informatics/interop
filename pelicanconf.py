import glob
from pathlib import Path

from pelican.settings import DEFAULT_CONFIG
from pelican.readers import MarkdownReader

config = DEFAULT_CONFIG.copy()

AUTHOR = 'Association for Pathology Informatics'
SITENAME = 'API Interoperability Resources'

# should not end with trailing slash
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
LINKS = (
    ('API home', 'https://www.pathologyinformatics.org/'),
    ('github issues', 'https://github.com/assoc-path-informatics/interop/issues'),
)

GITHUB_CORNER_URL = 'https://github.com/assoc-path-informatics/interop'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "./elegant"
THEME = "./Flex"
THEME_COLOR = 'light'

# place files replacing theme templates in ./content/templates
THEME_TEMPLATES_OVERRIDES = ['./content/templates']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

# custom variable indicating template links to include in nav
TEMPLATE_LINKS = ['categories', 'tags', 'archives']

# copied to /output without modification
STATIC_PATHS = ['images', 'css']

# these resources referenced as href="{{ SITEURL }}/{{ var }}"
SITELOGO = 'images/API-250px-300dpi.jpg'
FAVICON = 'images/favicon.ico'
CUSTOM_CSS = 'css/custom.css'

DISPLAY_PAGES_ON_MENU = True
# do not append page slug to urls for pages
DISABLE_URL_HASH = True

# # prevent Pelican from reading files matching the following patterns
IGNORE_FILES = ['.#*', 'includes', 'templates', 'README.md', '_*']

# render markdown contents from files in /content/includes and make
# accesible from INCLUDES variable in html templates
INCLUDES = {}
for fname in glob.glob('./content/includes/*.md'):
    pth = Path(fname)
    INCLUDES[pth.stem], _ = MarkdownReader(config).read(fname)

