from django.db import models

# Create your models here.

class ColorChoices(models.TextChoices):
    RED = "Red", "red"
    GREEN = "Green", "green"
    BLUE = "Blue", "blue"
    YELLOW = "Yellow", "yellow"
    BLACK = "Black", "black"
    WHITE = "White", "white"

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    manufacturer = models.ForeignKey("manufacture.Manufacture", on_delete=models.CASCADE, related_name="products")
    color = models.CharField(choices=ColorChoices.choices, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.color}"
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["created_at"]