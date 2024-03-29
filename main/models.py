from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Trip(TimeStampedModel):
    user = models.ForeignKey(User)
    date = models.DateField(blank=True, null=True,
               help_text="")
    odometer_start = models.FloatField(null=True, blank=True,
        help_text=(""))
    odometer_end = models.FloatField(null=True, blank=True)
    reason = models.CharField(max_length=1000, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def distance(self):
        start = self.odometer_start or 0
        end = self.odometer_end or 0
        return abs(end - start)

    def clean(self):
        if not self.odometer_start and not self.odometer_end:
            raise ValidationError('Oops, you have to fill out EITHER '
                                  'the odometer starting or ending values')

    def get_absolute_url(self):
        return reverse("edit", args=[self.id])

    def __unicode__(self):
        return "%s: %s : %s" % ("User", self.date, self.distance())

    class Meta:
        ordering = ['-date']
