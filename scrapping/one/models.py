from django.db import models

# Creating restaurant model with required fields
class Restaurant(models.Model):

    restaurant_name=models.CharField(max_length=254)
    restaurant_url=models.CharField(max_length=254)
    restaurant_location=models.CharField(max_length=254)
    restaurant_rating=models.CharField(max_length=254)

    def __str__(self):
        return self.restaurant_name
