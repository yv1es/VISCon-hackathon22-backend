

from ast import arg
from django.db import models

from backend.sendmails import sendNotification
from django.db.models.signals import m2m_changed

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    iconUrl = models.CharField(max_length=200, blank=True, null=True)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return self.name

class MailSubs(models.Model):
    mailAddress = models.EmailField()
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return self.mailAddress

class Tag(models.Model):
    name = models.CharField(max_length=20)
    iconUrl = models.CharField(max_length=200, blank=True, null=True)
    id = models.AutoField(primary_key = True)

    subscribers = models.ManyToManyField(MailSubs, blank=True)

    def __str__(self):
        return self.name

class Organizer(models.Model):
    name = models.CharField(max_length=20)
    organizerUrl = models.URLField(blank=True, null=True)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    shortDescription = models.TextField()
    description = models.TextField()
    price = models.TextField(blank=True, null=True)

    eventStart = models.DateTimeField()  
    eventEnd = models.DateTimeField(blank=True, null=True)  

    registrationStart = models.DateTimeField(blank=True,null=True)  
    registrationEnd = models.DateTimeField(blank=True, null=True)  

    image = models.ImageField(blank=True, upload_to='event_images')                         #difference to icon?
    id = models.AutoField(primary_key = True)
    link = models.URLField(blank=True, null=True)

    categories = models.ManyToManyField(Category, related_name='events', blank=True)
    tags = models.ManyToManyField(Tag, related_name='events', blank=True)
    organizers = models.ManyToManyField(Organizer, related_name='events', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class HasBeenNotified(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(MailSubs, on_delete=models.CASCADE)
    

def handleM2MChange(sender, instance, action, reverse, model, pk_set, **kwargs):
    # print(action)
    # print(pk_set)
    if not action == "post_add":
        return

    interestedPeople = set()
    for id in pk_set:
        tag = Tag.objects.get(pk=id)
        for sub in tag.subscribers.all():
            print(sub)
            interestedPeople.add(sub)
    
    # print(interestedPeople)

    for receiver in interestedPeople:
        #check if he already got a mail
        notification, created =  HasBeenNotified.objects.get_or_create(event=instance, subscriber=receiver)

        if created:
            sendNotification([receiver.mailAddress], instance)
            print("notified " + receiver.mailAddress)
        else:
            pass
            # print("user " + receiver.mailAddress + " already got notification")

m2m_changed.connect(handleM2MChange, sender=Event.tags.through)

    