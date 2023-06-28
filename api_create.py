import requests
import json

values = {
   "local_part": "omrozh",
   "domain": "grandassembly.net",
   "name": "Ömer Özhan",
   "quota": "3072",
   "password": "05082004Oo",
   "password2": "05082004Oo",
   "active": "1",
   "force_pw_update": "1",
   "tls_enforce_in": "1",
   "tls_enforce_out": "1"

}

headers = {
  'Content-Type': 'application/json',
  'X-API-Key': '6D7225-0F9EE4-10D41D-F59E72-F746BA'
}

request = requests.post('http://mail.grandassembly.net/api/v1/add/mailbox', data=json.dumps(values), headers=headers)

response_body = request.content
print(response_body)
