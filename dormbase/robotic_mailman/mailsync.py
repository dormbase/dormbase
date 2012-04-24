# for every group, we create a corresponding mailman list.
# we set the admin members of the group to be the list generated
# by recursively iterating up from the owner of the group under consideration
from dormbase.core.models import Resident
from dormbase.core.models import Group, GroupMember
import robotic_mailman

domainSuffix = '@mit.edu'

def mailsync(group):
    '''Returns True if group sync succeeded; False otherwise.'''
    robotic_mailman.deleteList(group.mailingListName)
    # TODO, adjust admin email and password
    robotic_mailman.newList(group.mailingListName, 'root@simmons.mit.edu', 'password')
    emails = [m.athena + domainSuffix for m in group.members.all() \
                  if GroupMember.objects.get(group = group, member = m).autoMembership]
    robotic_mailman.addMembers(group.mailingListName, emails)

    result = robotic_mailman.listMembers(group.mailingListName)
    print result

    if set(result.split('\n')) != set(emails):
        return False
    return True

def all_email_sync():
    for g in Group.objects.all():
        robotic_mailman.deleteList(g.mailingListName)
        robotic_mailman.newList(g.mailingListName, 'root@simmons.mit.edu', 'password')
        print [m.athena + domainSuffix for m in g.members.all()]
        robotic_mailman.addMembers(g.mailingListName, [m.athena + domainSuffix for m in g.members.all()])
        ownerSet = list(recursive_get_group_owners(g, []))
        print 'set list owner ' + g.mailingListName + ' -> ' + str(list(ownerSet))
        robotic_mailman.resetModerators(g.mailingListName, list(ownerSet))
        print 'finished adding list ' + g.mailingListName

def recursive_get_group_owners(g, L):
    if g == None or g.owner == None:
        return L
    print str(g) + ' is owned by ' + str(g.owner)
    owners = [m.athena + domainSuffix for m in g.owner.members.all()]
    print 'owners: ' + str(owners)
    L += owners
    print 'L now ' + str(L)
    return L
    # TODO: not currently recursive
    #for owner in g.owner:
    #    recursive_get_group_owners(owner, L)
