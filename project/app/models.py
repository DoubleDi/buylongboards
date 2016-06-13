from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Item(models.Model):
    name = models.CharField("name", max_length = 50)
    price = models.PositiveIntegerField(blank = True, null = True)
    oldprice = models.PositiveIntegerField(blank = True, null = True)
    picture = models.ImageField(upload_to="to/", blank=True, verbose_name="picture")
    site = models.URLField(blank = True)
    charac = models.TextField("characteristics", blank = True, null = True)
    komp = models.PositiveIntegerField("kompaktnost", blank = True, null = True)
    speed = models.PositiveIntegerField("speed", blank = True, null = True)
    upr = models.PositiveIntegerField("upravlyaemost", blank = True, null = True)
    ust = models.PositiveIntegerField("ustoychivost", blank = True, null = True)
    amor = models.PositiveIntegerField("amortization", blank = True, null = True)
    gib = models.PositiveIntegerField("gibkost", blank = True, null = True)


    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
    def __str__(self):
        return self.name

