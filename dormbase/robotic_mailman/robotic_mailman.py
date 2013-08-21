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

import os
import subprocess
import tempfile

def sanitize(s):
    return s

def getMailmanPath():
    return '/usr/lib/mailman/bin/'

def genericMailmanCall(args):
    '''Returns None if the call failed, else returns the output'''
    if len(args) < 2:
        raise Exception('attempted to make mailman call without arguments')
    try:
        # remove empty arguments
        args = map(sanitize, [x for x in args if len(x) != 0])
        cmd = ' '.join([getMailmanPath() + args[0]] + map(sanitize, args[1:]))
        print cmd
        return subprocess.check_output([getMailmanPath() + args[0]] + args[1:])
    except subprocess.CalledProcessError as c:
        print 'Exception while calling mailman with arguments: ' + str(args)
        print 'return code: ' + str(c.returncode)
        print 'output: ' + c.output
        return None

def validate(listname, usernames):
    if len(listname) == 0:
        raise Exception('listname must not be empty!')
    if not type(usernames) == type(list()):
        raise Exception('usernames must be array!')

# note: listnames are forced to be lowercase!
def newList(listname, adminEmail, adminPassword):
    if sum(int(x.isupper()) for x in listname) != 0:
        raise Exception('list names must be lowercase')
    return genericMailmanCall(['newlist', '--quiet', listname, adminEmail, adminPassword])

def deleteList(listname, deleteArchivesToo = False):
    if deleteArchivesToo:
        return genericMailmanCall(['rmlist', flag, listname])
    return genericMailmanCall(['rmlist', listname])

def addMembers(listname, usernames, digest = False):
    validate(listname, usernames)
    tf = tempfile.NamedTemporaryFile('w')
    for u in usernames:
        tf.write(u + '\n')
    tf.flush()
    fileType = '--digest-members-file=' if digest else '--regular-members-file='
    r = genericMailmanCall(['add_members', fileType + tf.name, listname])
    # returns output of form 'Subscribed: john@example.com\nSubscribed: mike@example.com'
    tf.close() # also does delete, see subprocess docs
    return r

def listMembers(listname, onlyRegular = False, onlyDigest = False, onlyNomail = False):
    flagC = int(onlyRegular) + int(onlyDigest) + int(onlyNomail)
    if flagC > 1:
        raise Exception('only one flag option can be specified when showing list members')
    flag = ['', '--regular', '--digest', '--nomail'][flagC]
    members = genericMailmanCall(['list_members', flag, listname])
    return members.rstrip() # remove trailing \n

def removeMembers(listname, usernames, notifyUsers = True, notifyAdmin = True):
    validate(listname, usernames)
    flags = []
    if not notifyUsers:
        flags += ['--nouserack']
    if not notifyAdmin:
        flags += ['--noadminack']
    return genericMailmanCall(['remove_members', listname] + flags + usernames)

def resetModerators(listname, newmoderators):
    if not 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] = ''
    old = os.environ['PYTHONPATH']
    os.environ['PYTHONPATH'] += os.getcwd() + '/add_moderators.py'
    print os.environ['PYTHONPATH']
    import add_moderators
    genericMailmanCall(['withlist', '-l', '-r', 'add_moderators', listname, ','.join(newmoderators)])
#    os.environ['PYTHONPATH'] = old
