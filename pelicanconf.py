AUTHOR = 'mb256'
SITENAME = "mb256's blog"
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'
THEME = '../pelican-themes/bootstrap2-dark'

RELATIVE_URLS = True

STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed(s)
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
#RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('mbrouk', 'https://mbrouk.pythonanywhere.com/'),
		 ('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
