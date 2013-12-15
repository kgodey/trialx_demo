import requests
from trialx.models import ClinicalTrial, ClinicalTrialSite

TRIALX_API_URL = 'http://trialx.com/query'


def find_trial_matches(**kwargs):
	search_params = kwargs
	search_params['op'] = 'json'
	search_params['start'] = requests.get(TRIALX_API_URL, params=search_params).json()['total']
	return requests.get(TRIALX_API_URL, params=search_params).json()


def add_trial(trialdict):
	trial = ClinicalTrial(title = trialdict['Title'], url = trialdict['Url'], trialx_id = trialdict['Id'], source = trialdict['Source'], phase = trialdict['Phase'], condition = trialdict['Condition'])
	if trialdict['StudyType'] == 'Observational':
		trial.study_type = 'O'
	elif trialdict['StudyType'] == 'Interventional':
		trial.study_type = 'I'
	trial.save()
	trial_sites = []
	for site in trialdict['Sites']:
		trial_site = ClinicalTrialSite(sitename = site['sitename'], address = site['address'], city = site['city'], state = site['state'], zipcode = site['zip'])
		trial_site.trial = trial
		trial_site.save()
		trial_sites.append(trial_site)
	return trial


def add_all_trials(trialsdict):
	trials = []
	for trialdict in trialsdict['ClinicalTrials']:
		trials.append(add_trial(trialdict))
	return trials


def find_and_add_trials(**kwargs):
	trialsdict = find_trial_matches(**kwargs)
	trials = add_all_trials(trialsdict)
	return trials