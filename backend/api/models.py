from django.db import models
from django.contrib.auth.models import User
from util.models import DateTimeMixin, IsActiveMixin
from django.utils.translation import ugettext_lazy as _
from api.accounts.models import UserProfile


class Block(DateTimeMixin):
    """A block represents a unit of time, dedicated towards a goal.
    """
    # The content of the block
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(_('description'), max_length=3000,
                               default='', null=True, blank=True)





