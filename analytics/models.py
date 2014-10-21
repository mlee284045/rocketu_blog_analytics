from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return '{}'.format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    country = models.CharField(max_length=40)

    class Meta:
        unique_together = ('city', 'country', 'region')

    def __unicode__(self):
        return '{}'.format(self.city)


class View(models.Model):
    page = models.ForeignKey(Page, related_name='views')
    location = models.ForeignKey(Location, related_name='views', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    longitude = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    def __unicode__(self):
        return '{}, {}'.format(self.page, self.location)