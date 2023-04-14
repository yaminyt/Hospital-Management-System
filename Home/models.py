from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name= models.CharField (max_length=100)
    dep_description= models.TextField(max_length=200)
    def __str__(self):
        return self.dep_name


class doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.TextField(max_length=200)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE) 
    doc_image=models.ImageField(upload_to="Doctor")
    
    def __str__(self):
        return "Dr. " + self.doc_name + "-("+self.doc_spec +")"

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=12)
    p_email=models.EmailField(max_length=20)
    doc_name=models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    
class Confirmation(models.Model):
    name= models.CharField(max_length=250)
    
        
    

    