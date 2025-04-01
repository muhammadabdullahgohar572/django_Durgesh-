from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)

    def __str__(self):
        return f'This is an Employee named {self.name} and Department is {self.department}'


class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField();
    picture=models.ImageField(upload_to="testimonial/")
    rating=models.IntegerField()
    
    def __str__(self):
        return self.testimonial
    