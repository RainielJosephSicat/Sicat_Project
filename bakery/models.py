from django.db import models


class BreadCategories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BreadProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(BreadCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BreadPost(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.name


class CustomerInfo(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CustomerMessage(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.customer.name}"
