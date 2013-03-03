from django.db import models
from django import forms
from dormbase.core.models import Resident

# Create your models here.
class Guest(models.Model):
    resident = models.ForeignKey(Resident)

    # Must supply either a username or a fullname or both
    athena = models.CharField(max_length = 8, verbose_name = "athena id", null = True)
    fullname = models.CharField(max_length = 256, null = True)

    date_start = models.DateField(null = True)
    date_end = models.DateField(null = True)

    notes = models.TextField(null = True)

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
