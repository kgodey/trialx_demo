from django.db import models


class ClinicalTrial(models.Model):
	STUDY_TYPE_CHOICES = (
		('O', 'Observational'),
		('I', 'Interventional'),
		('U', 'Unknown')
	)
	title = models.TextField()
	url = models.URLField()
	source = models.TextField(blank=True)
	trialx_id = models.IntegerField()
	phase = models.CharField(max_length=1, blank=True)
	study_type = models.CharField(max_length=1, choices=STUDY_TYPE_CHOICES, default='U')
	condition = models.TextField(blank=True)


class ClinicalTrialSite(models.Model):
	sitename = models.TextField()
 	address = models.TextField(blank=True)
	city = models.CharField(max_length=255, blank=True)
	state = models.CharField(max_length=255, blank=True)
	zipcode = models.IntegerField(max_length=5, blank=True)
	trial = models.ForeignKey(ClinicalTrial)
