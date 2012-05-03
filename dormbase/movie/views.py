# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render_to_response, RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from dormbase.movie.models import Movie, Genre
from dormbase.core.models import Resident
from random import sample

from django.http import HttpResponse, HttpResponseRedirect, Http404

import json

def movie_detail(request, movieId):
    payload = {'movie': Movie.objects.get(imdbId = movieId)}
    return render_to_response('movie/movieDetail.html', payload, context_instance=RequestContext(request))

def movie_reserve(request):
    if request.method == 'POST':
        id = request.POST['imdbId']
        m = Movie.objects.get(imdbId = id)
        m.available = False
        # This is to test desk worker dashboard. Replace with resident
        # who is making request.
        m.checkedOutBy = Resident.objects.order_by('?')[0]
        m.save()
        
        movie = json.dumps({
                    'title': m.canonicalTitle,
                    'checkedOutBy': m.checkedOutBy.getFullName(),
                    })
        print movie
        return HttpResponse(movie, mimetype='application/json')

    raise Http404

def movie_get(request):
    if request.method == 'GET':
        movies = []
        for m in Movie.objects.filter(available = False):
            movies.append({
                    'title': m.canonicalTitle,
                    'checkedOutBy': m.checkedOutBy.getFullName() if m.checkedOutBy != None else None
                    })

        return HttpResponse(json.dumps(movies), mimetype='application/json')

def genre_get(request, genreType, viewType):
    genresFilter = Genre.objects.get(name = genreType)
    movies = Movie.objects.filter(genres = genresFilter).order_by('title')

    if viewType == 'gallery':
        viewType = True
    else:
        viewType = False

    payload = {'genre' : genreType, 'viewType': viewType, 'movies': movies}
    return render_to_response('movie/genre.html', payload, context_instance=RequestContext(request))

def genre_list(request):
    genreList = ['Action',
                 'Adventure',
                 'Comedy',
                 'Drama',
                 'Horror',
                 'Sci-Fi',
                 'Romance',
                 'Thriller']

    new = Movie.objects.filter(genres = Genre.objects.get(name = 'New')).order_by('?')
    newAdditions = new[0:min(5, len(new))]

    payload = {'genres' : genreList, 'newAdditions': newAdditions}
    return render_to_response('movie/movieHome.html', payload, context_instance=RequestContext(request))

