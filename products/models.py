from django.db import models

# Create your models here.
class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(unique=True,max_length=50)
    description = models.TextField()
    price = models.FloatField(blank=False, default=0.99)
    image = models.ImageField(upload_to="product-images/")

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
