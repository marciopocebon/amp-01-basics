import requests
import json

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

url = 'https://api.amp.cisco.com/v1/event_streams'

headers = {'content-type': 'application/json'}

data = {'name':'Threat Detected','event_type':[1090519054],'group_guid':['bfe6abd0-6591-4bf2-a0d3-02efc1cd268e']}

request = requests.post(url, headers=headers, auth=(amp_client_id, amp_api_key), data=json.dumps(data))

print(request.json())
