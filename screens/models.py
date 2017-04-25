from __future__ import unicode_literals

from django.db import models
from input_forms.models import InputForm


# class to hold global screen widget configuration
class ScreenWidget(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    configuration = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ScreenWidget"
        verbose_name_plural = "ScreenWidgets"


class Screen(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    input_forms = models.ManyToManyField(InputForm)
    screen_widgets = models.ManyToManyField(ScreenWidget)
    layout = models.TextField()
    theme = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"


# class to hold global screen widget data
# the same configuration can produce and consume different data
# i.e a widget to show open-nti graphs can be configured for an
# open-nti instance, but different data for each different graph
class ScreenWidgetData(models.Model):
    widget_type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ScreenWidgetData"
        verbose_name_plural = "ScreenWidgetData"
