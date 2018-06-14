# coding=UTF-8

"""
Base mixins for models


Created on 6/14/18

@author: 'bingxinfan'
"""

from django.db import models


class DateTimeMixin(models.Model):

    """
    This is a datetime mixin for models
    should allow model have some datetime log functionality.
    user your own judgement, do not duplicate the fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IsActiveManager(models.Manager):

    def get_queryset(self):
        return super(IsActiveManager, self).get_queryset().filter(
            is_active=True)


class IsActiveMixin(models.Model):

    """
    This allows set active flag to the object
    And protect the date never got deleted
    """
    is_active = models.BooleanField(default=True)

    objects = IsActiveManager()

    class Meta:
        abstract = True

    def delete(self, fake=True):
        if fake:
            self.is_active = False
            self.save()
        else:
            super(IsActiveMixin, self).delete()
