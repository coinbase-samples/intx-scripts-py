# Copyright 2023-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json, hmac, hashlib, time, requests, base64, os, uuid
from urllib.parse import urlparse

url = 'https://api.international.coinbase.com/api/v1/orders'

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SIGNING_KEY = os.environ.get('SIGNING_KEY')
PASSPHRASE = os.environ.get('PASSPHRASE')

timestamp = str(int(time.time()))
method = 'POST'

client_order_id = uuid.uuid4()
side = 'BUY'
size = '1'
tif = 'GTC'
instrument = 'BTC-PERP'
order_type = 'LIMIT'
price = '100'

payload = {
   'client_order_id': str(client_order_id),
   'side': side,
   'size': size,
   'tif': tif,
   'instrument': instrument,
   'type': order_type,
   'price': price
}

url_path = urlparse(url).path
message = timestamp + method + url_path + json.dumps(payload)
hmac_key = base64.b64decode(SIGNING_KEY)
signature = hmac.digest(hmac_key, message.encode('utf-8'), hashlib.sha256)
signature_b64 = base64.b64encode(signature)

headers = {
   'CB-ACCESS-SIGN': signature_b64,
   'CB-ACCESS-TIMESTAMP': timestamp,
   'CB-ACCESS-KEY': ACCESS_KEY,
   'CB-ACCESS-PASSPHRASE': PASSPHRASE,
   'Accept': 'application/json',
   'content-type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
parse = json.loads(response.text)
print(json.dumps(parse, indent=3))
