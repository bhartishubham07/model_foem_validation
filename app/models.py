from django.db import models

from django.core import validators

# Create your models here.

G = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER')
]

class Student(models.Model):
    Name = models.CharField(max_length=30,validators=[validators.RegexValidator('[A-Z]'), validators.MaxLengthValidator(20)])
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20, choices=G)
    Mobile = models.CharField(max_length=10, validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10),validators.RegexValidator('[6-9]\d{9}')])
    Email = models.EmailField()
    Aadhar = models.CharField(max_length=30,validators=[validators.MaxLengthValidator(12),validators.MinLengthValidator(12),validators.RegexValidator('\d{12}')])
    
    def __str__(self):
        return self.Name