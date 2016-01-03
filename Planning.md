Things to do
============

Since the API will not handle User registration, the UI site must be handle registration. So far the application has several components:

* Admin Site - Django
* API Database
* Contributor UI - Django
* Android App - For Readers
* Web Reader - For Readers

The API and the Contributor UI exist at the same resource location.

Here are some things I have not yet accounted for:

* Sharing translations
* Reversions
* Groups

Priority Items for Version 0.1
------------------------------

1. Build the Contributor UI site
	a. Registration, Login, Logout
	b. User Control Panel - Authenticated
		a. List of Chapters that belong to this User, grouped by Series
		b. Ability to edit the chapters that belong to this User
		c. Ability to delete the chapters that belong to this User
		d. Ability to add a new chapter
	c. User Control Panel - Staff
		a. Ability to CRUD Series
		b. Ability to browse all chapters, grouped by series
2. Build a minimal Android app
	a. Index of Series
	b. View Series Detail, with a list of chapters listed
	c. Read a chapter
	
How does the android app work?
------------------------------

Whenever anything is downloaded, it is cached in the local memory of the device. 

Whenever the device is prompted, it can query to refresh content by finding out what content has changed.

Here is an array of all series and the dates they (or any of its component chapters) were last changed.
{
[
'1':'timestamp', 
'2':'timestamp',
]
}

Here is an array of all the chapters within a series and the dates they were last changed:
{
[
'23':'timestamp',
'43':'timestamp',
]
}

So the procedure is as follows:

1. Android does regular query of series and their most recent changes
2. Using the dictionary returned, compare which series have changed data
3. Send more requests to the series endpoint to figure out which chapters have changed
4. Get the chapters that have changed

Functions:

* Get_all_changed_series_after_DATE
* Get_all_changed_chapters_that_belong_to_series_after_DATE