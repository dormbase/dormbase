from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import random

class TestUser():
    def __init__(self):
        self.username = 'userEx'
        self.location = ''
        self.perish = 'No'

def desk_worker(request):
    packages = []
    bins = ['A', 'B', 'C', 'D', 'Floor']

    for i in xrange(1, random.randint(4,10)):
        u = TestUser()
        u.username += str(i)
        print u.username
        u.location = bins[random.randint(0, (len(bins) - 1))]
        packages.append(u)

    payload = {'packages': packages}

    return render_to_response('package/package.html', payload, context_instance = RequestContext(request))
