from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    married = models.BooleanField(default=False)

    def __str__(self):
        return self.name
