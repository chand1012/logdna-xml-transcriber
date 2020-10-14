import requests
from requests.auth import HTTPBasicAuth
import time
import os

from requests.exceptions import RequestException
from jsonl import loads

def get_logs(key=os.environ.get('SERVICE_KEY'), to_time=time.time(), from_time=(time.time()-86400), size=100, level='', apps='', additional_params=''):
    req_url = f"https://api.logdna.com/v1/export?to={to_time}000&from={from_time}000&size={size}"
    if level:
        req_url += f"&level={level}"
    if apps:
        req_url += f"&apps={apps}"
    if additional_params:
        req_url += additional_params

    resp = requests.get(req_url, auth=HTTPBasicAuth(key, ''))
    if resp.status_code == 200:
        return loads(resp.content.decode())
    
    raise RequestException(f'Error {resp.status_code}: {resp.content}')

if __name__=='__main__':
    print(get_logs())