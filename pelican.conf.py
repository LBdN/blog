# -*- coding: utf-8 -*-
AUTHOR = u'Lionel Barret de Nazaris'
SITENAME = u"LBdN's musings"
SITEURL = 'http://blog.pythonneers.org'
TIMEZONE = "Europe/Paris"

GITHUB_URL = 'http://github.com/LBdN/'
DISQUS_SITENAME = "blog-LBdN"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 4

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Biologeek', 'http://biologeek.org'),
         ('Filyb', "http://filyb.info/"),
         ('Libert-fr', "http://www.libert-fr.com"),
         ('N1k0', "http://prendreuncafe.com/blog/"),
         (u'Tarek Ziadé', "http://ziade.org/blog"),
         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('twitter', 'http://twitter.com/LBdN'),
          ('github', 'http://github.com/LBdN'),
          ('linkedin', 'http://fr.linkedin.com/pub/lionel-barret-de-nazaris/3/328/a41'),
          )


# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
