from django.db import models

# Create your models here.
class Prestamos (models.Model):
    loan_id = models.IntegerField()
    loan_type=models.TextField()
    loan_date=models.TextField()
    loan_total=models.IntegerField()
    customer_id=models.IntegerField()