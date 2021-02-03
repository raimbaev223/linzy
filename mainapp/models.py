from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class ProductQuerySet(models.QuerySet):

    def find_by_title(self, title):
        return self.filter(title__icontains=title)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().filter(in_archive=False)

    def find_by_title(self, title):
        return self.get_queryset().find_by_title(title)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='CategoryName', verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Товар')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_archive = models.BooleanField(default=False)
    prod = ProductManager()

    class Meta:
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


