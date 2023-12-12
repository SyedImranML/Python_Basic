from django.db import models

# from .models import Register  # Import your user model


class Register(models.Model):
    u_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    add = models.CharField(max_length=60)
    dob = models.DateField()
    mob = models.IntegerField()


class Transaction(models.Model):
    user = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    limit = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    reqwithdraw = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return f"{self.user.u_name}"



