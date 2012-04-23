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
