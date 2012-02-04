from django.db import models

class AbstractRoom(models.Model):
    """
    Abstract class containing all non-dorm-specific room attributes. 
    """
    number = models.CharField(max_length = 100)
    metaInformationForLocating = models.CharField(max_length = 1000)
    phone = models.CharField(max_length = 20)    

    def __unicode__(self):
        return self.number

    class Meta:
        abstract = True

class Room(AbstractRoom):
    """
    This class contians room attributes which are dorm-specific.
    """
    grtSection = models.CharField(max_length = 100)

class AbstractUser(models.Model):
    """
    Abstract class containing all non-dorm-specific user attributes. 
    """
    room = models.ForeignKey(Room)
    firstname = models.CharField(max_length = 200, verbose_name="first name")
    lastname = models.CharField(max_length = 200, verbose_name="last name")
    athena  = models.CharField(max_length = 200, verbose_name="athena id") # no "@mit.edu" suffix
    altemail = models.EmailField(verbose_name="non-MIT email")
    url = models.CharField(max_length = 1000)
    about = models.TextField()
    active = models.BooleanField()
    livesInDorm = models.BooleanField()
    year = models.IntegerField()
    
    def __unicode__(self):
        return self.firstname + ' ' + self.lastname

    class Meta:
        abstract = True

class User(AbstractUser):
    """
    This class contians user attributes which are dorm-specific.
    """
    title = models.CharField(max_length = 50)
    cell = models.CharField(max_length = 20)
    hometown = models.CharField(max_length = 200)

class Group(models.Model):
    autoSync = models.BooleanField() # auto mailing list sync
    mailingList = models.CharField(max_length = 200)
    owner = models.ForeignKey("self")
    members = models.ManyToManyField(User, through='GroupMembers')

    def __unicode__(self):
        return self.mailingList

class GroupMembers(models.Model):
    member = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    isAdmin = models.BooleanField()
    position = models.CharField(max_length = 200) # used for government positions. can be null
    autoMembership = models.BooleanField() # true if sync'd to this group via script
