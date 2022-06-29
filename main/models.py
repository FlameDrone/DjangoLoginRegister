from django.db import models

# Create your models here.
class Table(models.Model):
    tableName = models.CharField(max_length=255)
    def __str__(self):
        return self.tableName

class User(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name