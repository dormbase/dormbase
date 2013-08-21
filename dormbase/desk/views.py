# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import forms
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from dormbase.package.models import PackageForm
from dormbase.movie.models import MovieForm
from dormbase.core.models import Resident
from dormbase.personal.models import Guest
import autocomplete_light
autocomplete_light.autodiscover()

from . import autocomplete_light_registry

class GuestSigninForm(forms.Form):
    guest = forms.ModelChoiceField(
        Guest.objects.all(),
        widget=autocomplete_light.ChoiceWidget(
            "GuestSigninAutocomplete",
            attrs={'placeholder': 'Username or full name'}))

def dashboard(request):
    pf = PackageForm()
    mf = MovieForm()
    payload = {'packageForm': pf, 
               'movieForm': mf,
               'guestForm': GuestSigninForm()}

    return render_to_response('desk/dashboard.html', payload, context_instance = RequestContext(request))
