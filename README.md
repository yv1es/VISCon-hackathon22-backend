# "Application Name here" - Backend

This project composes the backend of the whole application.
It handles requests by users/admins to deliver and change data about the events.

## techstack

The data is being hosted on a postgress server which is managed by a django instance.
Gunicorn hosts the django instance and is itself connected to the port 80 via Nginx.

## Setup

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

## Usage

Admins accounts are able to add, modify and remove events, tags and categories.
Users will be able to poll this data which can then be sorted and filtered to inform about upcomming events
hosted by different student bodies at eth.

## API

Get all events:
<ip>/api/events/

Get all events for given category:
<ip>/api/events/?category_id=<category_id>

Get all categories:
<ip>/api/categories/

Get all tags:
<ip>/api/tags/
