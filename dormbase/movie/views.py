from django.shortcuts import render_to_response, RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from dormbase.movie.models import Movie, Genre

from django.http import HttpResponse, HttpResponseRedirect, Http404

def list_movies(request):
    payload = {'movies' : Movie.objects.all()}
    print payload
    return render_to_response('movie/movies.html', payload, context_instance=RequestContext(request))
