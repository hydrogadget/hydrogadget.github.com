#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"HydroGadget"
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
SITENAME = u"HydroGadget"
SITEURL = 'http://hydrogadget.org'
#SITESUBTITLE = 'The Raspberry Pi Powered Irrigation System'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

GOOGLE_ANALYTICS = 'UA-36766611-1'
GITHUB_URL = 'https://github.com/hydrogadget/'
TWITTER_USERNAME = 'hydrogadget'
TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Blog'
DATE_FORMATS = {
    'en': '%a, %b %d %Y',
}

DELETE_OUTPUT_DIRECTORY = True
THEME = 'hydrogadget-theme'
LOGO = 'http://i.imgur.com/hk8mdQr.png'

# Blogroll
LINKS =  (
         ('RaspberryPi.org', 'http://raspberrypi.org'),
         ('SYN Shop', 'http://synshop.org'),
         ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('Python.org', 'http://python.org'),
)

# Social widget
SOCIAL = (
         ('twitter', 'http://twitter.com/hydrogadget'),
         ('imgur', 'http://hydrogadget.imgur.com'),
)

DEFAULT_PAGINATION = 10
