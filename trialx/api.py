import requests

TRIALX_API_URL = 'http://trialx.com/query'

def find_trial_matches(**kwargs):
	search_params = kwargs
	search_params['op'] = 'json'
	print search_params
	trial_matches = requests.get(TRIALX_API_URL, params=search_params)
	print trial_matches.url
	return trial_matches.json()