from django.shortcuts import render
from models import ClinicalTrial

def random_trial(request):
	trial = ClinicalTrial.objects.order_by('?')[0]
	return render(request, 'trialx/trial_detail.html', {'trial': trial})
