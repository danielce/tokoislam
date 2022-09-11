#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Islam'
BLOG_AUTHORS = 'Islam'
SITENAME = 'Mega promocje'
SITESUBTITLE = 'Promocje na okrągło'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

PLUGINS = [
    'extended_sitemap',
    'neighbors',
]

# Social widget
SOCIAL = (
    ('663663618', 'https://telinfo.co/pl/numer/663663618/'),
    ('player za granicą za darmo', 'https://technetblog.pl/2020/12/jak-ogladac-tvn-player-i-ipla-za-granica-2018/'),
)


DEFAULT_PAGINATION = 20

COPYRIGHT = "Tokoislam - Wszelkie prawa zastrzezone"



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/daniel/projects/pelican/themes/nice-blog"
