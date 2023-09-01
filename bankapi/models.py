from django.db import models



class Banks(models.Model):
    ifsc = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_id= models.CharField(max_length=100)
    branch = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ifsc
    
    
