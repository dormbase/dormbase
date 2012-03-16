""" This file populates test packages """

from dormbase.core.models import Resident
from dormbase.package.models import Package
import random

def import_test_packages():
    residents = Resident.objects.all()[0:random.randint(5, 15)]

    for r in residents:
        if random.randint(0,5) == 5:
            o = True
        else:
            o = False
        
        l = random.choice(['A', 'B', 'C', 'D', 'Floor'])
    
        p = Package(recipient = r,
                    perishable = o,
                    location = l)
        p.save()

    print 'Packages COMPLETE'
