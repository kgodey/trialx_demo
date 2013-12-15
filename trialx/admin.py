from django.contrib import admin
from models import ClinicalTrial, ClinicalTrialSite

admin.site.register((ClinicalTrial, ClinicalTrialSite))
