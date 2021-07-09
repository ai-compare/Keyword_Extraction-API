import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works
#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'} 

# Select API
url = 'https://api.edenai.run/v1/pretrained/text/keyword_extraction'

# Select providers, and text to analyze
payload = {'providers': '[\'ibm\', \'microsoft\', \'aws\']','text':'I am angry today', 'keywords_to_find': 'neutral','language': 'en-US'}

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
