from django.db import models

class Product(models.Model):
    owner = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name
    

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=255) 
    link = models.URLField(max_length=255)
    duration = models.BigIntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.lesson_name


class User(models.Model):
    name = models.CharField(max_length=255) 
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    wathed_time = models.BigIntegerField()
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.BooleanField()