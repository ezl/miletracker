from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.localflavor.us.models import USStateField
from django.contrib.auth.models import User

class UserProfile(TimeStampedModel):
    user = models.ForeignKey(User)
    email = models.EmailField(null=True, blank=True)
    state = USStateField(null=True, blank=True)

    def __unicode__(self):
        return self.user.username
