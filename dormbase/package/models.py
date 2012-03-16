from django.db import models
from django.contrib.auth.models import User as AuthUser
from dormbase.core.models import Resident

class Package(models.Model):
    recipient = models.ForeignKey(Resident, null = True)
    perishable = models.BooleanField()
    date_recieved = models.DateField(auto_now_add = True)
    #checked_in_by = models.ForeignKey(AuthUser, null = True, blank = True) # Set to true for development
    #checked_out_by = models.ForeignKey(AuthUser, null = True, blank = True) # Set to true for development
    location = models.CharField(max_length=16)

    def __unicode__(self):
        return self.recipient
