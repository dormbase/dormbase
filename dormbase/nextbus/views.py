from django.http import HttpResponse
import lxml.etree
import datetime
import json

# Info on Nextbus api:
# http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

baseNextBusURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&'

def nextbus(request):
    agency = 'mit'

    now = datetime.datetime.now()
    tech_start = now.replace(hour=6,  minute=15, second=0) 
    tech_end = now.replace(hour=7,  minute=10, second=0) 

    if  now > tech_start and now < tech_end:
        route = 'tech'
        stop = 'simmhl'

    else:
        route = 'saferidecambwest'
        stop = 'simmhl'
    
    data = lxml.etree.parse(baseNextBusURL + 'a=' + agency + '&r=' + route + '&s=' + stop)
    next_times = [prediction.get('minutes') for prediction in data.findall('.//predictions/direction/prediction')]
    jsonout = json.dumps(next_times, sort_keys=True, indent=4)
    print jsonout
    return HttpResponse(jsonout, mimetype="application/json")
