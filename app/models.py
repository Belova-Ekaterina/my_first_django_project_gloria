from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование")
    country = models.CharField(max_length=255, null=False, blank=False, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование")
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Родительская категория")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Описание")
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    image_url = models.URLField(max_length=300, null=False, blank=False, verbose_name="URL изображения")
    category = models.ForeignKey("Category", null=False, blank=False, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.ForeignKey("Brand", null=False, blank=False, on_delete=models.CASCADE, verbose_name="Бренд")

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta():
        verbose_name = "Товар"
        verbose_name_plural = "Товары"