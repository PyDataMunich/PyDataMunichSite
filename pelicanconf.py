#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyData Munich'
SITENAME = 'PyData Munich'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('PyData', 'https://pydata.org'),
         ('Python.org', 'http://python.org/'),
         )

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = [('Meetup Group', 'https://www.meetup.com/PyData-Munchen/'),
              ('Github Repos', 'https://github.com/PyDataMunich'),
]

ABOUT_ME = 'We are a local group that meets regularly throughout Munich to learn data science, incorporating free and accessible tutorials, an engaging community, and delicious pizza and beer. Join us at our next event!'

# Social widget
# SOCIAL = (('Meetup Group', 'https://www.meetup.com/PyData-Munchen/'),
#           ('Our Github Repositories', 'https://github.com/PyDataMunich'),)

DEFAULT_PAGINATION = 10

# Nick-added

THEME = './themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# PLUGINS = ['assets', 'sitemap', 'gravatar']



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
