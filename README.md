### project Creation date and README file  25 Mar 2020.


### BikeShare Statistical Data
Simple small Python project to give the user some Statistical information,
about the bikeshare Co. in three major cities in USA

### Description
Use of Python to explore data related to bike share systems
for three major cities in the United States — Chicago, New York City, and Washington.


### Files used
Used three main files contains metadata for both Trips and Stations.

- washington.csv
- new_york_city.csv
- chicago.csv

Metadata:

Start Time: day and time trip started, in CST
End Time: day and time trip ended, in CST
Trip Duration: time of trip in seconds 
Start Station: name of station where trip originated
End Station: name of station where trip terminated 
User Type: "Customer" is a rider who purchased a 24-Hour Pass; "Subscriber" is a rider who purchased an Annual Membership
Gender: gender of rider 
Birth Year: birth year of rider

Notes:

* First row contains column names
* Trips that did not include a start or end date are excluded
* Trips less than 1 minute in duration are excluded
* Trips greater than 24 hours in duration are excluded
* Gender and birthday are only available for Subscribers

Used one main Python file contains all the script.
- (bike_share.py)

used to make interactive dialoge with user to retreive some statistical data as:
- chossing the City to deal with.
- defining which month or all months within the Data Set.
- defining which day or all days of the week.
- gives the user some data about the frequency of usage 'month, day, time, staion...'
- gives the user some calculations about the timing and travle time ...
- gives the user of the project the users type for the bikes (customer - Dependent - subscriber)
### Usage

1- Clone the project repository:
	$ git clone https://github.com/mfezzat/pdsnd_github.git

2- install python
	windows: install python by download and run '.exe' file
	linux  : $ sudo apt-get insatll python
	
3- run the project
	$ python python bike_share.py
	
### Credits

https://python4astronomers.github.io/installation/packages.html

https://pymotw.com/3/

https://docs.python.org/3/library/index.html

https://git-scm.com/book/en/v2

https://www.atlassian.com/git/tutorials/using-branches

https://docs.google.com/document/d/1DoNBEQJyGHi0qAWpMpQM9lU9_VKh8ubdOY2BmKdvZcc/edit

https://github.com/udacity/pdsnd_github

https://stackoverflow.com/questions/10565217/do-you-push-every-single-commit
