from django.db import models


class ClinicalTrial(models.Model):
	STUDY_TYPE_CHOICES = (
		('O', 'Observational'),
		('I', 'Interventional'),
	)
	title = models.TextField()
	url = models.URLField()
	source = models.TextField()
	trialx_id = models.IntegerField()
	phase = models.CharField(max_length=1)
	study_type = models.CharField(max_length=1, choices=STUDY_TYPE_CHOICES)
	condition = models.TextField()


class ClinicalTrialSite(models.Model):
	sitename = models.TextField()
 	address = models.TextField()
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	zipcode = models.IntegerField(max_length=5)
	trial = models.ForeignKey(ClinicalTrial)
