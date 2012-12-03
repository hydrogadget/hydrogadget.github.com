#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"HydroGadget"
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
SITENAME = u"HydroGadget"
SITEURL = 'http://hydrogadget.org'

GOOGLE_ANALYTICS = 'UA-36766611-1'
GITHUB_URL = 'https://github.com/hydrogadget/'
TWITTER_USERNAME = 'hydrogadget'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Blog'

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS =  (
         ('RaspberryPi.org', 'http://raspberrypi.org'),
	 ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('Python.org', 'http://python.org'),
)

# Social widget
SOCIAL = (
         ('twitter', 'http://twitter.com/hydrogadget'),
         ('imgur', 'http://hydrogadget.imgur.com'),
)

DEFAULT_PAGINATION = 10

# I dont think this works the way I thought it would.
# Sadface.

LOGOTEXT = 'HydroGadget'
#LOGOIMAGE = '/theme/images/hydrogadget.png'
LOGOIMAGE = 'http://i.imgur.com/g6huB.png'
