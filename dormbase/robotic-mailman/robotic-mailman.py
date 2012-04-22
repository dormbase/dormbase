# robotic-mailman
# independent python interface to mailman using subprocess
# Isaac Evans (c) 2012

#import envoy
import subprocess
import tempfile

def sanitize(s):
    return s

def getMailmanPath():
    return '/usr/lib/mailman/bin/'

def genericMailmanCall(args):
    '''Returns None if the call failed, else returns the output'''
    if len(args) < 2:
        raise Exception('Exception: attempted to make mailman call without arguments')
    try:
        # remove empty arguments
        args = filter(lambda x: len(x) != 0, args)
        cmd = ' '.join([getMailmanPath() + args[0]] + map(sanitize, args[1:]))
        print cmd
#        return envoy.run(cmd, data = None, timeout=10).std_out
        return subprocess.check_output([getMailmanPath() + args[0]] + map(sanitize, args[1:]))
    except subprocess.CalledProcessError as c:
        print 'Exception while calling mailman with arguments: ' + str(args)
        print 'return code: ' + str(c.returncode)
        print 'output: ' + c.output
        return None

# note: listnames are forced to be lowercase!
def newList(listname, adminEmail, adminPassword):
    if sum(int(x.isupper()) for x in listName) != 0:
        raise Exception('list names must be lowercase')
    return genericMailmanCall(['newlist', '--quiet', listname, adminEmail, adminPassword])

def deleteList(listname, deleteArchivesToo = False):
    if deleteArchivesToo:
        return genericMailmanCall(['rmlist', flag, listname])
    return genericMailmanCall(['rmlist', listname])

def addMembers(listname, usernames, digest = False):
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
    if len(listname) == 0:
        raise Exception('listname must not be empty!')
    flags = ''
    if not notifyUsers:
        flags += '--nouserack'
    if not notifyAdmin:
        flags += '--noadminack'
    return genericMailmanCall(['remove_members', listname, flags, ''.join(usernames)])
