from getNext10 import *
import webbrowser
import requests
import uuid
def startServer():
    print("Poggin confirmed")
    # data = makeRequest()
    # processedData = makeReadable(data)
    # url = "http://127.0.0.1:5500/webpage/index.html?data="
    
    # webbrowser.open(url, new=0, autoraise=True)
    

def makeNotiChannel():
    channelID = str(uuid.uuid4())
    print("Channel ID: "+channelID)
    jsonContent = {
    "id": channelID, # Your channel ID.
    "type": "web_hook",
    "address": "http://127.0.0.1:5000/notify", # Your receiving URL.
    }



def makeReadable(data):
    stringOfData = ""
    for event in data:
        start = event['start'].get('dateTime', event['start'].get('date'))


def makeRequest():
    arrOfEvents = main()

    if arrOfEvents != 0:
        for event in arrOfEvents:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

        return arrOfEvents
    else:
        print("no events found.")
    


# startServer()

