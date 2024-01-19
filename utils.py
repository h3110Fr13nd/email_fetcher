import requests
import json
import pandas as pd
from io import StringIO
import subprocess

def check_container():
    cmd = "docker ps -q -f name=standalone-chrome"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip() != ''

def check_and_run_docker():
    cmd_run = "docker run -d -p 4444:4444 -p 7900:7900 -p 5900:5900 --shm-size=2g --name=standalone-chrome selenium/standalone-chrome"
    if not check_container():
        print("Docker container not found, running...")
        subprocess.run(cmd_run, shell=True)
        print("Docker container running")
    else:
        print("Docker container already running")

def get_proxies():
    url = 'https://free-proxy-list.net'
    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}
    df = pd.read_html(StringIO(requests.get(url, headers=header).text))[0]
    df = df[df['Https']=='yes']
    proxies = df['IP Address'] + ':' + df['Port'].astype(str)
    return proxies.to_list()


def clear_sessions(session_id=None):
    """
    Here we query and delete orphan sessions
    docs: https://www.selenium.dev/documentation/grid/advanced_features/endpoints/
    :return: None
    """
    url = "http://127.0.0.1:4444"
    if not session_id:
        # delete all sessions
        r = requests.get("{}/status".format(url))
        data = json.loads(r.text)
        for node in data['value']['nodes']:
            for slot in node['slots']:
                if slot['session']:
                    id = slot['session']['sessionId']
                    r = requests.delete("{}/session/{}".format(url, id))
    else:
        # delete session from params
        r = requests.delete("{}/session/{}".format(url, session_id))




