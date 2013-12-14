import requests

TRIALX_API_URL = 'http://trialx.com/query'

def find_all_trial_matches(**kwargs):
	search_params = kwargs
	search_params['op'] = 'json'
	search_params['start'] = requests.get(TRIALX_API_URL, params=search_params).json()['total']
	return requests.get(TRIALX_API_URL, params=search_params).json()
