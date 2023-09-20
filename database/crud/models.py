from django.db import models


# Create your models here.
class Employee(models.Model):
    empid = models.PositiveIntegerField(primary_key=True)
    empname = models.CharField(max_length=100, blank=False,db_column="ename")
    email = models.EmailField(blank=False, unique=True)
    class Meta:
        db_table="emp"
