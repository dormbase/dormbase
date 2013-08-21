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

from django.db import models
from django.contrib.auth.models import User as AuthUser
from django import forms
from dormbase.core.models import Resident

class Package(models.Model):
    BINS = (('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('F', 'Floor'))

    recipient = models.ForeignKey(Resident, null = True)
    location = models.CharField(max_length=8, choices=BINS)
    perishable = models.BooleanField()
    date_recieved = models.DateField(auto_now_add = True)
    hidden = models.BooleanField(default = False)
    #checked_in_by = models.ForeignKey(AuthUser, null = True, blank = True) # Set to true for development
    #checked_out_by = models.ForeignKey(AuthUser, null = True, blank = True) # Set to true for development

    def __unicode__(self):
        return unicode(self.recipient)

class PackageForm(forms.ModelForm):
    BINS = (('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('F', 'Floor'))

    location = forms.ChoiceField(choices=BINS)

    class Meta:
        model = Package
        exclude = ('date_received', 'hidden')
