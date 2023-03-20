# VISCon Hackathon Backend

During the 2022 VISCon Hackathon we developped a event planer application. The backend provides an API with all the event information and an admin backend to manage the events. 


## Usage

Admin accounts are able to add, modify and remove events, tags and categories.
Users will be able to poll event data which can then be sorted and filtered to inform about upcomming events
hosted by different student bodies at ETH.

## API

Get all events:
<host>/api/events/

Get all events for given category:
<host>/api/events/?category_id=<category_id>

Get all categories:
<host>/api/categories/

Get all tags:
<host>/api/tags/
