from django.db import models

class Debit(models.Model):
    debit_ID = models.AutoField(primary_key = True)
    debit_Amount = models.FloatField()
    debit_Description = models.TextField(max_length = 100, null = True)
    debit_User = models.TextField(choices =(
        ("M", "Mamá"),
        ("S", "Sofia"),
        ("D", "Daniela"),
        ("G", "Gabriela"),
        ("C", "Casa")
    ))
    debit_Date = models.DateField()