from django.contrib.auth.models import User
from dormbase.core.models import Resident
from dormbase.core.models import Room
from dormbase.core.models import Group
from dormbase.core.models import GroupMember
import random
import robotic_mailman    

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

def make_fake_groups():
    nerds = Resident.objects.all()[0:5]
    topnerd = Resident.objects.all()[0]
    g = Group(name = 'tech-chair',
              mailingListName = 'tech-chair',
              autoSync = True,
              owner = None,
              memacl = None)
    g.save()
    nn = GroupMember(member = topnerd, group = g, position = "Tech Chair", autoMembership = True)
    nn.save()

    g2 = Group(name = 'simmons-tech',
              mailingListName = 'simmons-tech',
              autoSync = True,
              owner = g,
              memacl = None)
    g2.save()
    for n in nerds:
        gm = GroupMember(member = n, group = g2, position = "Tech Committee Member", autoMembership = True)        
        gm.save()

    print 'two groups created'

def all_email_sync:
    for g in Group.objects.all():
        robotic_mailman.deleteList(g.mailingListName)
        robotic_mailman.newList(g.mailingListName)
        robotic_mailman.addMembers(g.mailingListName, g.members)
        recursive_set_group_owners(g)
        print 'finished adding list ' + g.mailingListName

def recursive_set_group_owners(g):
    if g.owner == None:
        return
    print 'set list owner ' + g.mailingListName + ' -> ' + str(g.owner.members)
    robotic_mailman.resetModerators(g.mailingListName, g.owner.members)
    recursive_set_group_owners(g.owener)

    
    
