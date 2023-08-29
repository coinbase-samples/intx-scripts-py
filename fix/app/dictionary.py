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
last_order_id = ''
last_client_order_id = ''
last_product_id = ''
last_side = ''
last_quantity = ''

FIELD_MSGTYPE = 35
MSGTYPE_EXECUTION_REPORT = '8'
MSGTYPE_REJECT = '3'
MSGTYPE_LOGON = 'A'

FIELD_EXECTRANSTYPE = 20
EXECTRANSTYPE_NEW = '0'

FIELD_SENDINGTIME = 52
FIELD_MSGSEQNUM = 34
FIELD_TARGETCOMPID = 56
FIELD_SYMBOL = 55
FIELD_TEXT = 58

FIELD_EXECTYPE = 150
EXECTYPE_NEW = '0'
EXECTYPE_PARTIAL = '1'
EXECTYPE_FILL = '2'
EXECTYPE_DONE = '3'
EXECTYPE_CANCELLED = '4'
EXECTYPE_STOPPED = '7'
EXECTYPE_REJECTED = '8'
EXECTYPE_RESTATED = 'D'
EXECTYPE_STATUS = 'I'

FIELD_CLORDID = 11
FIELD_ORDER_ID = 37
FIELD_QUANTITY = 151
FIELD_RETURN_QUANTITY = 38
FIELD_SIDE = 54
FIELD_PRODUCT_ID = 55

FIELD_EXPIRE_TIME = 126
FIELD_TARGET_STRATEGY = 847

FIELD_PASSWORD = 554
FIELD_USERNAME = 553
FIELD_RAWDATA = 96
FIELD_ACCESSKEY = 9407
FIELD_CANCELORDERSONDISCONNECT = 8013

TIME_IN_FORCE_GTT = '6'

STRATEGY_LIMIT = 'L'

SIDE_BUY = '1'
SIDE_SELL = '2'

TAG_NEW_ORDER = '20=0'
TAG_TEXT = '58='

DELIMITER = ''
