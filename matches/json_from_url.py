import requests
''' connect to the a url and return a json formatted database'''


def read_data_form_url(url):
    return requests.get(url).json()




