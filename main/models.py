from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse

# Create your models here.

class Trip(TimeStampedModel):
    date = models.DateField(blank=True, null=True,
               help_text="Defaults to today's date.")
    odometer_start = models.FloatField(null=True, blank=True,
        help_text=("You can just use the last 4 digits of the "
                   "odometer."))
    odometer_end = models.FloatField(null=True, blank=True,
        help_text=("If you're just starting your trip, you can "
                   "fill this in later, when the trip actually ends."))
    reason = models.CharField(max_length=1000, null=True, blank=True,
        help_text=("Optional. You can also fill it in later "
                   "if you want."))
    notes = models.TextField(null=True, blank=True,
        help_text="Optional.")

    def distance(self):
        start = self.odometer_start or 0
        end = self.odometer_end or 0
        return abs(end - start)

    def get_absolute_url(self):
        return reverse("edit", args=[self.id])

    def __unicode__(self):
        return "%s: %s : %s" % ("User", self.date, self.distance())

    class Meta:
        ordering = ['-date']
