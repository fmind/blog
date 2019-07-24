SITENAME = 'In [*]: F(mind)'
SITEURL = 'https://fmind.me'
AUTHOR = 'Médéric Hurier (fmind)'
IMAGE = 'images/avatar.png'
DESC = 'Doctor, Hacker, Learner, Teacher, Researcher, Entrepreneur, Father, and Dog Owner.'

GITHUB = 'fmind'
TWITTER = 'fmindme'
LINKEDIN = 'fmindme'

CACHE_CONTENT = True

THEME = 'theme/fmind'
THEME_STATIC_DIR = '.'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

STATIC_PATHS = [
    'files',
    'images',
]

DEFAULT_METADATA = {
    'image': IMAGE,
    'author': AUTHOR,
    'status': 'published',
    'category': 'objectivism',
}

EXTRA_PATH_METADATA = {
    'files/CNAME': {
        'path': 'CNAME',
    },
}

TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_FEED_RSS = ''
TAG_FEED_ATOM = ''

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_FEED_RSS = ''
AUTHOR_FEED_ATOM = ''

CATEGORY_SAVE_AS = ''
CATEGORY_FEED_RSS = ''
CATEGORY_FEED_ATOM = ''
CATEGORIES_SAVE_AS = ''

PAGE_LANG_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ''
TRANSLATION_FEED_RSS = ''
TRANSLATION_FEED_ATOM = ''

ARCHIVES_SAVE_AS = ''
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = 'atom.xml'
RSS_FEED_SUMMARY_ONLY = False
