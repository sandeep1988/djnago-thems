from django.db import models
from django.core.urlresolvers import reverse
#from products.models import Product
import products

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_edit', kwargs={'pk': self.pk})