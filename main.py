import requests
import json

url = "https://api.fda.gov/drug/label.json?limit=1"

data = requests.get(url).json()

print(json.dumps(data, indent=4))