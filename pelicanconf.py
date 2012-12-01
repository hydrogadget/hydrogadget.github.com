#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"HydroGadget"
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
SITENAME = u"HydroGadget"
SITEURL = ''

GITHUB_URL = 'https://github.com/hydrogadget/'
TWITTER_USERNAME = 'hydrogadget'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Blog'

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS =  (
	 ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('RaspberryPi.org', 'http://raspberrypi.org'),
         ('Python.org', 'http://python.org'),
)

# Social widget
SOCIAL = (
         ('twitter', 'http://twitter.com/hydrogadget'),
)

DEFAULT_PAGINATION = 10
