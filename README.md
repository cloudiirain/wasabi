Project Wasabi
==============

"A light novel translation host that isn't wordpress."

Synopsis
--------

Currently, there are no dedicated or specialized applications designed to host novels. Wordpress is the most common
light novel host, but it is by no means ideal, especially since most wordpress sites are extremely insular. Mediawiki 
(used by Baka-Tsuki) is another major alternative, but it is critized by members of the translation community 
because the content is publicly available for editing. 

Project Wasabi seeks to synthesize these two approaches. The goal is to provide a platform where translators can 
upload their translations in one place, but still allow content creators to control who has editing access to their
translations. Translations can be private, public, shared with certain individuals or entire groups, etc.

The desired result is something akin to fanfiction.net or fictionpress.net, but with an increased focus on
collaborative work and creating a standardized novel directory.

Lastly, a major goal of Project Wasabi is to provide a free and public API, with the hope that this project can be
extended and built upon. Possible extensions could include smartphone apps, automatic EPUB/PDF generators, and much
more.

Implementation Details
----------------------

Django REST Framework (Python) will be used for writing an API that will be the skeleton of the framework. 
 
The web application will also be served by Django, but frontend logic will be handled by Jquery or Angular (TBD).


Design Version 0.1
==================

User Stories
------------

As a reader, I would like to view an ordered list of series a use this for navigation.

As a reader, I would like to view a series page which contains a list of ordered translations (chapters) within it.

As a reader, I would like to read a translation chapter and easily be able to navigate to the next chapter.

As a prospective contributor, I would like to register.

As a contributor, I would like to login/logout.

As a contributor, I would like to have a dashboard that contains my translations and any translations that are shared
with me.

As a contributor, I would like to create/update/delete a translation chapter and designate whom I would like to share
access rights with.

As a contributor, I would like to revert to previous versions of a chapter.

As an administrator, I would like to create/update/delete a series.