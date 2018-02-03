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

# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    lock = models.BooleanField(default=False, blank=True)

    class Meta:
        abstract = True


###################################################################################################
# User
###################################################################################################

class UserData(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)
    address = models.TextField(blank=True, null=True)
    achievements = models.CharField(max_length=7)
    position = models.CharField(max_length=31, choices=POSITIONS, default='', blank=True)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.month_year