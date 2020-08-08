


## Problem Statement

The **JSON** file describes a list of users &amp; their corresponding periods of activity across multiple months.
>1. Design and implement a Django application with **User** and 	**ActivityPeriod** models
>2.	Write a **custom management** command to populate the database   with some dummy data
>3.	And design an API to serve that data in the **json** format given above.

## JSON Response
```
{
 	"ok": true,
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}
```

## Dummy-Data

Dummy-Data allows you to generate dummy data that fits a JSON specification.
**FAKER** is a Python package that generates fake data the database 
```
pip install faker
```
`faker.Faker()` creates and initializes a faker generator, which can generate data by accessing properties named after the type of data

## Usage
Enter the following command in the console after cloning the repository and migrating and create superuser 
```
python manage.py createsuperuser
```
enter Admin details such as
* Username: admin
* ID: admin
* TZ(time-zone): Asia/Kolkata
	* Asia/Kolkata is obtained from the pytz module `pytz.all_timezones`
* Real name: admin
* Password: admin


This creates a Superuser who's username and password is uesd when trying to access the endpoints.
```
python manage.py create_dummy_users
```
This populates the database with 50 **User** objects and 3 corresponding **Activity Period** objects for each of user objects



## API Endpoints

* https://www.website.com/list_paginated_users/
This endpoint provides a json response with pagination consisting of
	* count
		* Gives the total number of users including admin
	* next
		* Gives an endpoint to next page
	* previous
		*  Gives an endpoint to previous page
	* result 
		* Gives the **JSON response** as expected in the problrm statement
```
{
    "count": 51,
    "next": "http://127.0.0.1:8000/list_paginated_users/?page=4",
    "previous": "http://127.0.0.1:8000/list_paginated_users/?page=2",
    "results": [
        {
            "id": "ZAGAYXI1B",
            "real_name": "Laurie Howard",
            "tz": "('America/Halifax', 'America/Halifax')",
            "activity_periods": [
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                },
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                },
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                }
            ]
        },
        {
            "id": "3ROUUQEX0",
            "real_name": "Caitlin Wilson",
            "tz": "('Asia/Macao', 'Asia/Macao')",
            "activity_periods": [
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                },
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                },
                {
                    "start_time": "Sat 08 Aug 2020 04:17PM",
                    "end_time": "Sat 08 Aug 2020 04:17PM"
                }
            ]
        },
}
```
* https://www.website.com/list_all_users/
This endpoint provides a json response with the list of all users as the problem statement expects


## Default Username and Password
When prompted , enter Username as admin 
and password as admin.
Thiese are the credentials of the superuser