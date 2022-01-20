from django.db import models
from django.urls import reverse
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.template.defaultfilters import slugify

# Create your models here.

class Stock(models.Model):
    name = models.TextField(blank=False, null=False)
    quantity = models.IntegerField()
    buy_price = models.DecimalField(decimal_places=2, max_digits=10000)
    buy_date = models.DateField()
    updated = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    DisplayFields = ['name', 'quantity', 'buy_price', 'total', 'buy_date', 'updated']
    SearchableFields = ['name']

    class Meta:
        db_table = 'STOCKS'

    @property
    def total(self):
        total = self.quantity * self.buy_price
        return total
        

    def sum_of_total(self):
        total = 0
        for i in self.name.all():
            total += i.qty_price_mul()
        return total

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("portfolio:stock", kwargs={"my_name":self.slug})
        return reverse("portfolio:stock", kwargs={"my_name":self.slug})


class Gold(models.Model):
    grams = models.DecimalField(decimal_places=2, max_digits=10000)
    buy_price = models.DecimalField(decimal_places=2, max_digits=10000)

