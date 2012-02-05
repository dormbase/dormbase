from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response('index.html')
