# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
