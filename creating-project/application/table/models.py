from django.db import models


# Create your models here.
class TableField(models.Model):
    name = models.CharField(max_length=150)
    width = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class CsvFile(models.Model):
    path = models.CharField(max_length=200)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        return self.path
