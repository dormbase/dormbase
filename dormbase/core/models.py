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
from django.core.validators import validate_slug
from django.contrib.auth.models import User as AuthUser

class AbstractRoom(models.Model):
    """
    Abstract class containing all non-dorm-specific room attributes. 
    """
    number = models.CharField(max_length = 100)
    metaInformationForLocating = models.CharField(max_length = 1000, blank = True)

    def __unicode__(self):
        return self.number

    class Meta:
        abstract = True

class Room(AbstractRoom):
    """
    This class contians room attributes which are dorm-specific.
    """
    grtSection = models.CharField(max_length = 100, blank = True)

class AbstractResident(models.Model):
    """
    Abstract class containing all non-dorm-specific user attributes.
    Maintains a 1-1 with the auth app user module.
    """
    user = models.ForeignKey(AuthUser, unique = True)
    room = models.ForeignKey(Room)
    athena  = models.CharField(max_length = 8, verbose_name = "athena id") # no "@mit.edu" suffix
    year = models.IntegerField()
    altemail = models.EmailField(verbose_name="non-MIT email", blank = True)
    url = models.CharField(max_length = 256, blank = True)
    about = models.TextField(blank = True)
    livesInDorm = models.BooleanField()

    def __unicode__(self):
        return self.athena
    
    def getFullName(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        abstract = True

class Resident(AbstractResident):
    """
    This class contians user attributes which are dorm-specific.
    """
    title = models.CharField(max_length = 50, blank = True)
    cell = models.CharField(max_length = 20, blank = True)
    hometown = models.CharField(max_length = 200, blank = True)

    @models.permalink
    def get_absolute_url(self):
        return ('dormbase.personal.views.profile_username', (),
                {'username': self.athena})

class Group(models.Model):
    name = models.CharField(max_length = 200)
    mailingListName = models.CharField(max_length = 200, validators = [validate_slug])
    autoSync = models.BooleanField() # auto mailing list sync
    owner = models.ForeignKey("self", related_name = "groupOwner", blank = True, null = True)
    memacl = models.ForeignKey("self", related_name = "groupMemacl", blank = True, null = True)
    members = models.ManyToManyField(Resident, through='GroupMember')

    def __unicode__(self):
        return self.name

#    def save(self, *args, **kwargs):
#        if not mailingListNameOK(args['mailingListName']):
#            return
#        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.


class GroupMember(models.Model):
    member = models.ForeignKey(Resident)
    group = models.ForeignKey(Group)
    position = models.CharField(max_length = 200, blank = True, null = True) # used for government positions. can be null
    autoMembership = models.BooleanField() # true if sync'd to this group via script

    def __unicode__(self):
        return str(self.member) + ' -> ' + str(self.group)
