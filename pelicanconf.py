#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Krystopher Mathis'
SITENAME = 'krysmathis.com'
SITEURL = '/public'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


LINKS = (('Portfolio', 'http://krysmathis.com'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/krysmathis'),
          ('github', 'https://github.com/krysmathis'),
          ('twitter', 'https://twitter.com/coldbuckets'))
         

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10
THEME = "/Users/krystopher/workspace/portfolio-site/pelican-themes/Flex"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
