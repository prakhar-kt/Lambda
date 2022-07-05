import requests

def download_file(file):
    """Download the file passed as
    an argument from gharchive.org"""

    res = requests.get(f'https://data.gharchive.org/{file}')
    return res
