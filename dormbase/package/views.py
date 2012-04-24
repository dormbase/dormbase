from django.shortcuts import render_to_response
from dormbase.package.models import *
from django.http import HttpResponseRedirect, Http404, HttpResponse

import json

def package_get(request):
    if request.method != 'GET':
        raise Http404

    packages = []
    for p in Package.objects.filter(hidden=False):
        packages.append({
                'recipient': p.recipient.getFullName(),
                'location': p.location,
                'perishable': p.perishable,
                'id': p.id,
                })

    return HttpResponse(json.dumps(packages), mimetype='application/json')

def package_add(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            p = Package(recipient = cd['recipient'], 
                        location = cd['location'], 
                        perishable = cd['perishable'],)
            p.save()

            jsonPackage = json.dumps({'recipient': p.recipient.getFullName(),
                                      'location': p.location,
                                      'perishable': p.perishable,
                                      'id': p.id})

            return HttpResponse(jsonPackage, mimetype="application/json")

    raise Http404
            
def package_remove(request):
    if request.method == 'POST':
        p_id = request.POST['package_id']
        p = Package.objects.get(id = p_id)
        p.hidden = True
        p.save()
        pid = 'p' + str(p.id)
        jsonResponse = json.dumps({'id': pid})
        return HttpResponse(jsonResponse, mimetype="application/json")

    raise Http404
