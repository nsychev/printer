import os
import requests
import subprocess
import tempfile
import time

from config import *


def print_pdf(item):
    r = requests.get(f'{BASE_URL}/static/pdfs/{item}')
    assert r.status_code == 200
    with tempfile.TemporaryDirectory() as base_path:
        path = os.path.join(base_path, 'main.pdf')
        with open(path, 'wb') as f:
            f.write(r.content)
        subprocess.run(
            [PRINT_BIN, path, PRINTER]
        )
    
    r = requests.post(
        f'{BASE_URL}/api/jobs',
        data={'filename': item},
        headers={'Authorization': f'Bearer {TOKEN}'}
    )
    assert r.status_code == 200
    assert r.json() == {'result': 'ok'}

def get_pdfs():
    r = requests.get(
        f'{BASE_URL}/api/jobs',
        headers={'Authorization': f'Bearer {TOKEN}'}
    )
    assert r.status_code == 200
    return r.json()['result']


if __name__ == "__main__":
    while True:
        for item in get_pdfs():
            print_pdf(item)
        time.sleep(10)
        
