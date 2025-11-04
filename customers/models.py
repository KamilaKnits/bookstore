from django.db import models

# Create your models here.

# Customer clsss is table in the database
class Customer(models.Model):
    #the attributes (name and notes)are columns in the table
    #name and notes attributes are CharField and TextField (rows)
    name= models.CharField(max_length=120)
    notes= models.TextField()
    pic= models.ImageField(upload_to='customers', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
