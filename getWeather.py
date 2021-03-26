import requests
import json
import credentials

params = (
    ('expire_hours', '2'),
)
creds = credentials.Credentials()

data = '{"user":"'+creds.username+'", "password":"'+creds.password+'"}'
print(data)
resp_token = requests.post('https://pfa.foreca.com/authorize/token', params=params, data=data)
print(resp_token)
token_data = resp_token.json()
resp_token_json = json.loads(json.dumps(token_data))

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://pfa.foreca.com/authorize/token?expire_hours=2', data=data)


access_token = resp_token_json['access_token']

headers = {
    'Authorization': 'Bearer ' + access_token,
}

params = (
    ('lang', 'es'),
)

resp_tempe = requests.get('https://pfa.foreca.com/api/v1/current/100633679', headers=headers, params=params)
tempe_data = response_tempe.json()
resp_tempe_json = json.loads(json.dumps(tempe_data))
print(response_tempe_json)
print("Tällä hetkellä on", response_tempe_json['current']['temperature'], "astetta.")