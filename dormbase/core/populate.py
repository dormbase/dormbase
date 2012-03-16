from django.contrib.auth.models import User
from dormbase.core.models import Resident
from dormbase.core.models import Room
import random

def import_test_directory():
    f = open('core/test_names.txt')
    rooms = []    
    MAX_ROOM = 350
    for i in range(0, MAX_ROOM):
        r = Room(number = str(i), phone = str(random.randint(1111111111, 9999999999)))
        r.save()
        rooms.extend([r])

    print 'Room COMPLETE'

    for line in f.readlines():
        line = line.strip('\n')
        if '(' in line:
            continue
        line = line.split(' ')
        firstname, lastname = line[0], line[-1]
        if len(firstname) < 3 or len(lastname) < 3:
            continue
   #     print 'Adding ' + firstname + ' ' + lastname
        username = lastname[0:8].lower()
        print username
        u = User(first_name = firstname, last_name = lastname, username = username)
        u.save()
        r = Resident(user = u,
                     room = random.choice(rooms),
                     athena = username,
                     year = random.choice([2012, 2013, 2014, 2015]),
                     livesInDorm = True)
        r.save()

    print 'Residents COMPLETE'
