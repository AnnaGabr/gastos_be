from django.db import models

class Credit(models.Model):
    cred_ID = models.AutoField(primary_key = True)
    cred_Amount = models.FloatField()
    cred_Description = 	models.TextField(max_length = 100, null = True)
    cred_User = models.TextField(choices =(
        ("M", "Mamá"),
        ("S", "Sofia"),
        ("D", "Daniela"),
        ("G", "Gabriela"),
        ("C", "Casa")
    ))
    cred_Installment = models.IntegerField()
    cred_Date = models.DateField()