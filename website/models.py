from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # ✅ Name Field
    college = models.CharField(max_length=200)  # ✅ College Field
    age = models.IntegerField()  # ✅ Age Field
    is_Active = models.BooleanField(default=True)  # ✅ Active Status

    def __str__(self):
        return self.name
