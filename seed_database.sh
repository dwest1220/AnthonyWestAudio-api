#!/bin/bash

rm db.sqlite3
rm -rf ./audioapi/migrations
python3 manage.py makemigrations audioapi
python3 manage.py migrate
python3 manage.py migrate audioapi
python3 manage.py loaddata users
python3 manage.py loaddata inquiries
python3 manage.py loaddata staff
python3 manage.py loaddata booking
python3 manage.py loaddata bookingstaff
python3 manage.py loaddata services

