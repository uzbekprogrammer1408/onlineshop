from tabnanny import verbose
from django.db import models

# Create your models here.

class Kitobjanri(models.Model):
    name =  models.CharField(verbose_name="Janr nomi", max_length=30)

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"

    def __str__(self):
        return self.name

class Product(models.Model):
    janr = models.ForeignKey(Kitobjanri, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Kitob nomi", max_length=250)
    description = models.TextField(verbose_name="Kitob xaqida")
    price = models.FloatField(verbose_name="Kitob narxi")
    avtor = models.CharField(verbose_name="Kitob muallifi", max_length=50)
    image = models.ImageField(verbose_name="Kitob rasmi", upload_to="product_image")
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.name+" "+str(self.price)