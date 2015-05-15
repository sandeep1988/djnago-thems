from django.db import models
from django.core.urlresolvers import reverse
from categories.models import Category
import categories
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

class Product(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.IntegerField(default=000)
    points = models.IntegerField(default=0)
    notes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})