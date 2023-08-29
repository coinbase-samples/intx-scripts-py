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
import quickfix as fix
from app.fix_session import Application
from app.dictionary import FIELD_EXPIRE_TIME, FIELD_TARGET_STRATEGY, STRATEGY_LIMIT, TIME_IN_FORCE_GTT

class BuildCreate(Application):

    def create_order(self, fixSession):
        product = 'BTC-PERP'
        order_type = 'LIMIT'
        side = 'BUY'
        base_quantity = '1'
        limit_price = '10000'

        message = self.create_header(fixSession.portfolio_id, fix.MsgType(fix.MsgType_NewOrderSingle))
        message.setField(fix.Symbol(product))

        if order_type == 'MARKET':
            message.setField(fix.OrdType(fix.OrdType_MARKET))
            message.setField(847, 'M')
        elif order_type == 'LIMIT':
            message.setField(fix.OrdType(fix.OrdType_LIMIT))
            message.setField(fix.TimeInForce(TIME_IN_FORCE_GTT))
            message.setField(FIELD_EXPIRE_TIME, "20231001-00:00:10.000")
            message.setField(FIELD_TARGET_STRATEGY, STRATEGY_LIMIT)
            message.setField(fix.Price(float(limit_price)))
        message.setField(fix.Side(fix.Side_BUY if side == 'BUY' else fix.Side_SELL))
        message.setField(fix.OrderQty(float(base_quantity)))

        fixSession.send_message(message)
