from django.db import models

class Cash(models.Model):
    cash_ID = models.AutoField(primary_key = True)
    cash_Amount = models.FloatField()
    cash_Description = models.TextField(max_length = 100, null = True)
    cash_User = models.TextField(choices = (
        ("M", "Mamá"),
        ("S", "Sofia"),
        ("D", "Daniela"),
        ("G", "Gabriela"),
        ("C", "Casa")
    ))
    cash_Date = models.DateField()