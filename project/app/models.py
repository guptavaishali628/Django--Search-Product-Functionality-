from django.db import models

# Create your models here.
class AddCardData(models.Model):
    Name=models.CharField(max_length=40)
    Price=models.IntegerField()
    Company=models.CharField(max_length=50)
    Image = models.ImageField(upload_to='product_images/')