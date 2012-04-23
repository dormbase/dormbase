#!/usr/bin/env python

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
