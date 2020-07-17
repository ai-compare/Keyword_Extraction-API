import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#f7f665e0-7f52-4e5c-9ed1-abcfefd890f03

#Enter your API Token
headers = {  'x-access-token': 'Enter your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/api/v1/text/create/compare/keyword_extraction'

# Select providers, and text to analyze
payload = {'providers': '[\'ibm\', \'cognitives_service\', \'aws\']','text':'I am angry today', 'keywords_to_find': 'neutral','language': 'en-US'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
