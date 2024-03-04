from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.name
    