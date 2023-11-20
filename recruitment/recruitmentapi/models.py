from django.db import models

class recruitment(models.Model):
    name = models.CharField(max_length=100)
    personal_email = models.CharField(max_length=100)
    kiet_email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    mode_of_payment = models.CharField(max_length=100)
    library_id = models.CharField(max_length=100)
    desk = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    payment_status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name