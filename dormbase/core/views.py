from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def directory(request):
    payload = {}
    return render_to_response('core/directory.html', request, payload)

def directory_json(request):
    payload = {}
    import pdb
    pdb.set_trace()
#    prefix
    results = [Resident.objects.filter(athena__startswith = prefix)[:10]]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
