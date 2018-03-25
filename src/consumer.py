import requests

def get_status_code(url):
    return requests.get(url).status_code == 200