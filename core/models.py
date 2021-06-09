from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Staped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
