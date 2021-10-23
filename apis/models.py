from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Designation(object):
    DOCTOR = 'doctor'
    STAFF_USER = 'staff user'
    CHOICES = (
        (DOCTOR, 'doctor'),
        (STAFF_USER, 'staff user'))


class EventType(object):
    MEDICAL_TEST = 'medical test'
    OPD_TEST = 'opd test'
    CHOICES = (
        (MEDICAL_TEST, 'medical test'),
        (OPD_TEST, 'opd test'))



class User(AbstractUser):
    """
        Users within the Django authentication system are represented by this
        model.
    """
    designation = models.CharField(max_length=15, choices=Designation.CHOICES, default=Designation.STAFF_USER)


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PatientMedicalDetail(models.Model):
    patient_name = models.CharField(max_length=50)
    aadhaar_number = models.CharField(max_length=50)
    event = models.CharField(max_length=15, choices=EventType.CHOICES)
    file = models.FileField(upload_to ='uploads/')
    description = models.TextField()
    doctor = models.ForeignKey(User, on_delete=models.PROTECT)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)

    def __str__(self):
        return self.aadhaar_number

