###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _

from helpers.timestamp.models.timestamp import TimestampModel


###
# Model
###


class Movie(TimestampModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Title")
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    release_date = models.DateField(
        verbose_name=_("Release Date")
    )
    genre = models.TextField(
        verbose_name=_('Genre')
    )
    rating = models.FloatField(
        verbose_name=_("Rating")
    )

    def __str__(self):
        return self.title
