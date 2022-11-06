from ast import parse
from this import d
from unittest import skip
from django.core.management.base import BaseCommand, CommandError
from events.models import Event
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("hello from handle")
        events = scrapeVis()
        for e in events:
            newEvent = Event()
            newEvent.name = e["name"]
            newEvent.date = e["date"]
            newEvent.shortDescription = e["shortDescription"]
            newEvent.description = e["description"]
            newEvent.eventStart = e["eventStart"]
            newEvent.link = e["link"]
            newEvent.save()


        
def scrapeVis():

    url = 'https://vis.ethz.ch/en/events/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    event_columns = soup.find_all("div", class_="event-column")


    events = []

    def stripEnclosure(input):
        out = ""
        keep = True
        for c in input:
            if c == '<':
                keep = False
            

            if keep:
                out += c

            if c == '>':
                keep = True
        return out

    def parseDate(input):
        split = input.split(" ")
        date = ""
        for s in split:
            if s.__contains__("."):
                date = s
                break

        if date == "":
            print("error here")
        l = date.split(".")
        date = l[2] + "-" + l[1] + "-" + l[0]
        return date

    def trunkParticipate(input):
        out = ""
        end = False
        for c in input:
            if c == '#':
                end = True
            
            if not end:
                out += c
        return out

    for ec in event_columns:
        #ec contains one event
        e = {}
        

        l = ec.find("div", class_='card-title')
        if not l:
            continue


        title = stripEnclosure(str(l.findChild("h5")))

        print(title)

        txtFields = ec.find_all("p")
        parsedTxts = []
        for txt in txtFields:
            stripped = stripEnclosure(str(txt))
            if len(stripped) > 0:
                # print(stripped)
                parsedTxts.append(stripped)

        shortDescription = parsedTxts[0]
        eventStartTime = parsedTxts[2]
        eventEndTime = parsedTxts[3]

        #print(len(parsedTxts))
        # print(shortDescription)
        # print(eventStartTime)
        # print(eventEndTime)
        #print(parsedTxts[1]) useless
        # print(parsedTxts[4]) registration time
        
        l = ec.find("a", class_="no-style")
        link = "https://vis.ethz.ch" + trunkParticipate(l["href"])

        e["name"] = title
        e["date"] = parseDate(eventStartTime)
        e["shortDescription"] = shortDescription
        e["description"] = shortDescription #TODO change
        e["eventStart"] = parseDate(eventStartTime)
        e["eventEnd"] = parseDate(eventEndTime)
        e["link"] = link

        events.append(e)


    return events
