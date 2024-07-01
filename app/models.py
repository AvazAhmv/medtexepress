from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    icon = models.FileField(upload_to='app/icons/', verbose_name="Иконка")


class Product(models.Model):
    cat = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="product", verbose_name="Категория")
    code = models.CharField(max_length=250, verbose_name="Артикул")
    name = models.CharField(max_length=250, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    quanty = models.IntegerField(verbose_name="Количество")
    size = models.CharField(max_length=250, verbose_name="Объем")


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='app/images/products', verbose_name="Картинка")


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="properties")
    key = models.CharField(max_length=250, verbose_name="Название свойства")
    value = models.CharField(max_length=250, verbose_name="Значение свойства")


class ProductUsage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="usages")
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")


    