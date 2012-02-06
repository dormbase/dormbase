from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def home(request):
    return render_to_response('index.html', context_instance = RequestContext(request))
