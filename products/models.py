from django.db import models
from django.core.urlresolvers import reverse
from categories.models import Category
import categories

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=000)
    Quantity = models.IntegerField()
    category = models.ForeignKey(categories.models.Category)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})