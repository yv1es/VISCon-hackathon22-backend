# VISCon Hackathon Backend

During the 2022 VISCon Hackathon we developped a event planer application. The backend provides an API with all the event information and an admin backend to manage the events. 


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
