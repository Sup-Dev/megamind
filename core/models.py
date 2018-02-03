from django.conf import settings
from django.db import models

POSITIONS = (
    ('', ''),
    ('President', 'President'),
    ('Vice President Education', 'Vice President Education'),
    ('Vice President Membership', 'Vice President Membership'),
    ('Vice President Public Relations', 'Vice President Public Relations'),
    ('Secretary', 'Secretary'),
    ('Treasurer', 'Treasurer'),
    ('Sergeant at Arms', 'Sergeant at Arms'),
)

ROLES = (
    ('Evaluator', 'Evaluator'),
    ('TMOD', 'TMOD'),
    ('GE', 'GE'),
    ('TTM', 'TTM'),
    ('Timer', 'Timer'),
    ('Ah-Counter', 'Ah-Counter'),
    ('Grammarian', 'Grammarian'),
    ('Parliamentarian', 'Parliamentarian'),
)

VOTING_CATEGORIES = (
    ('Best Speaker', 'Best Speaker'),
    ('Best Evaluator', 'Best Evaluator'),
    ('Best Role Player', 'Best Role Player'),
    ('Best Supplementary Role Player', 'Best Supplementary Role Player')
)

CLUB_NAME = 'GTMC'


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    lock = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = True


########################################################################################################################
# User
########################################################################################################################

class UserData(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    address = models.TextField(blank=True, null=True)
    achievements = models.CharField(max_length=7)
    position = models.CharField(max_length=31, choices=POSITIONS, default='', blank=True)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user


########################################################################################################################
# Meeting
########################################################################################################################

class Meeting(BaseModel):
    number = models.PositiveSmallIntegerField()
    date = models.DateField()
    theme = models.CharField(default='', max_length=50)
    club_name = models.CharField(default=CLUB_NAME, max_length=30)
    home_club = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number) + ' - ' + self.club_name


class Speech(BaseModel):
    meeting = models.ForeignKey('Meeting', related_name='+', on_delete=models.PROTECT)
    speaker = models.ForeignKey('UserData', related_name='+', on_delete=models.PROTECT)
    topic = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    evaluator = models.ForeignKey('UserData', related_name='+', on_delete=models.PROTECT, null=True)


class Role(BaseModel):
    meeting = models.ForeignKey('Meeting', related_name='+', on_delete=models.PROTECT)
    role_player = models.ForeignKey('UserData', related_name='+', on_delete=models.PROTECT)
    role = models.CharField(max_length=15, choices=ROLES)


########################################################################################################################
# Voting
########################################################################################################################

class Winners(BaseModel):
    meeting = models.ForeignKey('Meeting', related_name='+', on_delete=models.PROTECT)
    category = models.CharField(max_length=30, choices=VOTING_CATEGORIES)
