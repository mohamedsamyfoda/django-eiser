from django.db import models


STATUS_TYPE = (
    ('Available','Available'),
    ('Not available','Not available'),
)


# Create your models here.
class Men(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    discount = models.CharField(max_length=50)
    price_now = models.IntegerField(default=0)
    Price_before = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name





