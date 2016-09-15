from __future__ import unicode_literals
from django.db import models

class returnTest(models.Model):
	patientID = models.CharField(max_length=50)
	accessCode = models.CharField(max_length=50)
	adress = models.CharField(max_length=50)

class applicantData(models.Model):
	PaccessCode = models.CharField(max_length=50)
	PPatientID = models.CharField(max_length=50)
	Padress = models.CharField(max_length=50)
	kitSent = models.BooleanField()
	kitRecieved = models.BooleanField()
