import requests
import json

base_uri = 'https://management.api.umbrella.com/v1'


def getDestinationLists(organizationId, management_key, management_secret):
    url = f'{base_uri}/organizations/{organizationId}/destinationlists'
    r = requests.get(url, headers={'Accept': 'application/json'}, auth=(management_key,management_secret))
    data = json.loads(r.content)
    print('''
***********************************************************************************************
*                                 Destination Lists Found                                     *
*_____________________________________________________________________________________________*
***********************************************************************************************
''')
    destinationLists = []
    for i in range(len(data['data'])):
        destinationLists.append(data['data'][i]['name'])
    print(*destinationLists, sep="\n")
    return(destinationLists)
    