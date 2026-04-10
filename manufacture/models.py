from django.db import models

class CountryChoices(models.TextChoices):
    GERMANY = "Germany", "germany",
    JAPAN = "Japan", "japan",

class Manufacture(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(choices=CountryChoices.choices, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.country}"

    class Meta:
        verbose_name = "Manufacture"
        verbose_name_plural = "Manufactures"
        ordering = ["created_at"]