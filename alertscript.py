#!/usr/bin/python
import argparse
import requests
import json

parser = argparse.ArgumentParser(description="Raises tickets in OSTicket")
parser.add_argument('summary',help='The issue summary that will appear in osTicket')
parser.add_argument('detail',help='The issue detail that will appear in osTicket')
args = parser.parse_args()

url = "https://<OSticket URL>/api/http.php/tickets.json"
key = "<OsTicket Api Key>"

data = {
"name":"Zabbix",
"email":"zabbix@<YOURDOMAIN>",
"phone":"111111111111",
"subject":args.summary,
"message":args.detail,
"topicId":"Zabbix",
"empresa":"Zabbix"
}

headers = {
"X-API-Key": key
}

r = requests.post(url,data=json.dumps(data),headers=headers)
print(r.text)
