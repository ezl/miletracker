from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Trip(TimeStampedModel):
    date = models.DateField(blank=True, null=True,
               help_text="")
    odometer_start = models.FloatField(null=True, blank=True,
               help_text="")
    odometer_end = models.FloatField(null=True, blank=True,
               help_text="")
    reason = models.CharField(max_length=1000, null=True, blank=True,
               help_text="")
    notes = models.TextField(null=True, blank=True,
               help_text="")

    # def get_absolute_url(self):
    #     return reverse("view_rental", args=[self.slug])

    def __unicode__(self):
        return "hi"
