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
import json, hmac, hashlib, time, requests, base64, os, sys
from urllib.parse import urlparse

if len(sys.argv) < 3:
    sys.exit('Usage: intx_get_order_details.py <portfolio> <id>')

portfolio = sys.argv[1]
id = sys.argv[2]

url = f'https://api.international.coinbase.com/api/v1/orders/{id}'

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SIGNING_KEY = os.environ.get('SIGNING_KEY')
PASSPHRASE = os.environ.get('PASSPHRASE')

timestamp = str(int(time.time()))
method = 'GET'

url_path = urlparse(url).path
message = timestamp + method + url_path
hmac_key = base64.b64decode(SIGNING_KEY)
signature = hmac.digest(hmac_key, message.encode('utf-8'), hashlib.sha256)
signature_b64 = base64.b64encode(signature)

headers = {
   'CB-ACCESS-SIGN': signature_b64,
   'CB-ACCESS-TIMESTAMP': timestamp,
   'CB-ACCESS-KEY': ACCESS_KEY,
   'CB-ACCESS-PASSPHRASE': PASSPHRASE,
   'Accept': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.status_code)
parse = json.loads(response.text)
print(json.dumps(parse, indent=3))
