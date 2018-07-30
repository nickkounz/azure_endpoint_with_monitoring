import os, json, requests
from datadog import initialize, api

api_key, app_key, *_ = open('secret.txt').read().split('\n')
if (api_key.startswith('*') and api_key.endswith('*')) or \
    (app_key.startswith('*') and app_key.endswith('*')):
    print('MISSING CONFIGURATION: the secret.txt file needs to be edited ' + \
        'to add api_key and app_key.')

def login_dg(options):
    initialize(**options)

def wirte_hb_warning():
    options = {
        'api_key': api_key,
        'app_key': app_key
    }
    login_dg(options)
    title = "AzS Heartbeat Alert"
    text = 'Azure Stack heartbeat test failed. This might cause by the Azure Stack availability or the API server itself. ' + \
    'You need to check the Azure Stack Portal to see whether this is an universual problem or an individual problem. ' + \
    'Please pay attention if you see this warning multiple times.'
    alert_type = 'warning'
    aggregation_key = "AzS Heartbeat Alert"
    source_type_name = "AZURE"
    tags = ['environment:azurestack_production']
    host = "Azure Function - [azs-heartbeat >> external_heartbeat]"
    api.Event.create(title=title,text=text,alert_type=alert_type,aggregation_key=aggregation_key,source_type_name=source_type_name,host=host,tags=tags)

def generate_report(url):
    try:
        response = requests.get(url)
        response_json = json.loads(response.text)
        result = response_json['TestResult']
        if str(result).strip() == "Success":
            pass
        else:
            wirte_hb_warning()
    except Exception:
        wirte_hb_warning()
 
if __name__ == "__main__":    
    url = "http://67.215.112.35:5000/heartbeat"
    generate_report(url)