from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import feedparser



def home(request):
    d = feedparser.parse('http://www.cafebonappetit.com/rss/menu/402') #should get cached and refreshed with a cron job
    payload = {'menu': d.entries[0].description}
    return render_to_response('index.html', payload, context_instance = RequestContext(request))
