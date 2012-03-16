""" This file populates test packages """

from dormbase.core.models import Resident
from dormbase.package.models import Package
import random

def import_test_packages():
    bins = ['A', 'B', 'C', 'D', 'Floor']
    
    residents = Resident.objects.all()[0:random.randint(5, 15)]

    for r in residents:
        if random.randint(0,5) == 5:
            o = True
        else:
            o = False
        
        l = bins[random.randint(0, (len(bins) - 1))]
    
        p = Package(recipient = r,
                    perishable = o,
                    location = l)
        p.save()
