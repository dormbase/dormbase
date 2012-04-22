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
    location = models.CharField(max_length=1, choices=BINS)
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
