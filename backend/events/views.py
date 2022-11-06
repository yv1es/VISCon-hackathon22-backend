

from unicodedata import category, name
from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from .models import Event, Category, Organizer, Tag, MailSubs
import datetime



# Create your views here.



def categories_endpoint(request):
    resp = get_all_categories()
    return JsonResponse(resp, status = 200)

def tags_endpoint(request):
    resp = get_all_tags()
    return JsonResponse(resp, status = 200)


def get_all_categories():

    resp = {
     "categories":[]    
    }

    for c in Category.objects.all():
        category_dict = category_to_dict(c)
        resp['categories'].append(category_dict)

    return resp


def get_all_tags():
    
    resp = {
     "tags":[]    
    }

    for t in Tag.objects.all():
        tag_dic = tag_to_dict(t)
        resp['tags'].append(tag_dic)
        
    return resp



def events_endpoint(request):
    
    # request should be ajax and method should be GET and have a 'searchTerm' parameter
    if request.method == "GET" and "category_id" in request.GET:

        # get the canonical_name and return 400 if empty
        category_id = request.GET.get("category_id", None)
        
        if not(category == None or not category):  
            resp = get_events_category(category_id)
            return JsonResponse(resp, status = 200)

    resp = get_all_events()
    return JsonResponse(resp, status = 200)
    
#TODO: this is not good, use at own risk!!
def mail_endpoint(request):
    print("mail_endpoint")
    if request.method == "GET":
        if not("mail_address" in request.GET): #and "tags" in request.GET):
            return HttpResponse(status = 420)

        mail_address = request.GET.get("mail_address", None)

        if "unsubscribe" in request.GET:
            print("deleting")
            #delete him from db
            try:
                go = MailSubs.objects.get(mailAddress=mail_address)
                go.delete()
            except MailSubs.DoesNotExist:
                go = None

            return HttpResponse(status = 200)

        tag_ids = request.GET.get("tag_ids", None)

        #do we know the address?
        mailsub, p = MailSubs.objects.get_or_create(mailAddress = mail_address) #should also save if needed

        for tag_id in tag_ids.split(','):
            tag = Tag.objects.get(id = int(tag_id))
            tag.subscribers.add(mailsub)

        
    return HttpResponse(status = 200)
    


def event_to_dict(event):
    e = {   'name': event.name,
             'shortDescription': event.shortDescription,
             'description': event.description,
             'price':'',
             'eventStart': event.eventStart,
             'eventEnd': '',
             'registrationStart': event.registrationStart,
             'registrationEnd': event.registrationEnd,
             'image' : '/event_images/default.jpg',
             'id' : event.id,
             'link' : '',
             'categories':[],
             'tags' : [],
             'organizers' : []

        }


    if event.image:
        e['image'] = event.image.name


    #TODO: add tests if value is present and only then try to access
    if event.price:
        e['price'] = event.price
    if event.eventEnd:
        e['eventEnd'] = event.eventEnd
    if event.registrationStart:
        e['registrationStart'] = event.registrationStart

    for t in event.tags.all():
        e['tags'].append(tag_to_dict(t))
    for c in event.categories.all():
        e['categories'].append(category_to_dict(c))
    for o in event.organizers.all():
        e['organizers'].append(organizer_to_dict(o))

    return e


def organizer_to_dict(organizer):
    o = {'name':organizer.name,
        'iconUrl': '',
        'id':organizer.id
        }
    if organizer.organizerUrl:
        o['organizerUrl'] = organizer.organizerUrl

    return o
        
def category_to_dict(category):
    c = {'name': category.name,
         'iconUrl': '',
         'id': category.id
        }
    if category.iconUrl:
        c['iconUrl'] = category.iconUrl

    return c

def tag_to_dict(tag):
    t = {'name': tag.name,
         'tagUrl': '',
         'id': tag.id}
    
    if tag.iconUrl:
        t['iconUrl'] = tag.iconUrl

    return t

def mailsubs_to_dict(mailsubs):
    m = {'mailaddr': mailsubs.mailaddr,
         'id': mailsubs.id}
    
    return m



def get_all_events():

    # response struct
    resp = {"events":[]    
    }

    for e in Event.objects.all():
        event_dict = event_to_dict(e)
        resp['events'].append(event_dict)
    
    return resp



def get_events_category(category_id):
    
    resp = { "events":[]   
    }

    for c in Category.objects.filter(id=category_id):
        
        #default values
        for e in c.events.all():
            event_dict = event_to_dict(e)
            resp['events'].append(event_dict)

    return resp


