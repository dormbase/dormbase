#!/usr/bin/env python

# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#from Mailman.Errors import NotAMemberError

def add_moderators(mlist, members):
    members = members.split(',')
    print members
    print mlist.moderator
    mlist.moderator = members
    mlist.Save()
#    try:
#        mlist.setMemberPassword(addr, newpasswd)
#        mlist.Save()
#    except NotAMemberError:
#        print 'No address matched:', addr
