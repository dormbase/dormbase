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
                'name': p.recipient.getFullName(),
                'bin': p.location,
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
            return HttpResponseRedirect('/desk')

        
    raise Http404
            
def package_remove(request):
    if request.method == 'POST':
        p_id = request.POST['package_id']
        p = Package.objects.get(id = p_id)
        p.hidden = True
        p.save()
        return HttpResponseRedirect('/desk')

    raise Http404
