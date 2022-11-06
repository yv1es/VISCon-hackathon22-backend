from django.contrib import admin
from .models import Event, Category, HasBeenNotified, Organizer, MailSubs, Tag

# Register your models here.
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Organizer)
admin.site.register(MailSubs)
admin.site.register(Tag)
admin.site.register(HasBeenNotified)