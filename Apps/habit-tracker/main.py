import requests
import datetime

USERNAME = 'kylef94'
TOKEN = 'kylessecrettoken'
endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{endpoint}/{USERNAME}/graphs'
graph_config = {
    'id' : 'codegraph',
    'name' : 'Coding Graph',
    'unit' : 'mins',
    'type' : 'int',
    'color' : 'sora',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
coding_graph_endpoint = f"{endpoint}/{USERNAME}/graphs/{graph_config['id']}"
coding_graph_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '90'
}

# response = requests.post(url=coding_graph_endpoint, json=coding_graph_config, headers=headers)
# print(response.text)
print(graph_endpoint)