import json
import requests
from bs4 import BeautifulSoup

url = 'https://cwe.mitre.org/data/definitions/20.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

bugs = []

# Extract bug information from HTML elements
for bug_elem in soup.find_all('div', class_='bug'):
    title = bug_elem.find('h2').text.strip()
    description = bug_elem.find('p', class_='description').text.strip()
    severity = bug_elem.find('span', class_='severity').text.strip()
    bugs.append({'title': title, 'description': description, 'severity': severity})

# Store bug information in a structured format (e.g., JSON)
with open('bugs.json', 'w') as f:
    json.dump(bugs, f)