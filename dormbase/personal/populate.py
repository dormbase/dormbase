from dormbase.personal.models import Guest
from dormbase.core.models import Resident
import random
import datetime

def import_test_guests():
    f = open('core/test_names.txt')
    names = [name.strip() for name in f.readlines()]

    # Choose one name to put on all the guests lists
    all_name = random.choice(names)

    for resident in Resident.objects.all()[0:5]:
        for name in random.sample(names, 5) + [all_name]:
            g = Guest(resident = resident,
                      athena = name.split(' ')[0].lower()[:8],
                      fullname = name)
            g.save()

    # Add a non-MIT person.
    g = Guest(resident = resident,
              fullname = "Random Guy")
    g.save()

    # Add a time-limited person.
    g = Guest(resident = resident,
              athena = "current",
              fullname = "Current Guest",
              date_end = datetime.datetime.now() + datetime.timedelta(weeks=1))
    g.save()
    g = Guest(resident = resident,
              athena = "future",
              fullname = "Future Guest",
              date_start = datetime.datetime.now() + datetime.timedelta(weeks=1))
    g.save()
    g = Guest(resident = resident,
              athena = "past",
              fullname = "Past Guest",
              date_end = datetime.datetime.now() - datetime.timedelta(weeks=1))
    g.save()

    print 'Guests COMPLETE'
