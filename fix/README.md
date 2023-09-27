# Coinbase International Exchange FIX README.md

This repository is a Python application for Coinbase's International Exchange (INTX) FIX API.
# Getting started

## 1. Gaining access

Clone the repository with the following command:
```
git clone https://github.com/coinbase-samples/intx-scripts-py
```

## 2. Configuration

You will need to install two dependencies for this to operate: quickfix and certifi. This allows for Python to successfully connect to Coinbase via FIX. From the root of the directory, this can be done with the following commands:

```
cd fix
pip install -r requirements.txt
```

We also want to store and grab variables to ensure connectivity to Exchange via FIX. To fill these values completely, you will need to generate an API key with trading functionality and also retrieve your portfolio ID, which is provided in the response of [List portfolios](https://docs.cloud.coinbase.com/intx/reference/getportfolios). Finally, your SVC_ACCOUNTID is identical to your ACCESS_KEY.  Populate the below and run the following to declare these variables:

```bash

export ACCESS_KEY=ACCESSKEYHERE
export PASSPHRASE=PASSPHRASEHERE
export SIGNING_KEY=SIGNING_KEYHERE
export PORTFOLIO_ID=PORTFOLIO_IDHERE
export SVC_ACCOUNTID=SVC_ACCOUNTIDHERE
export FIX_VERSION=FIX.4.2
export TARGET_COMP_ID=CBINTLOE
```

## 3. Running the application

Order details are configured inside `build_create_order.py`. Adjust order details in here, then place the order via the following command:

```
export order_dict=$(python client_create_order.py) 
```

The FIX application will connect to Coinbase, place the order with the provided order details, and then send a logout message to disconnect.

This saves critical order details to an environment variable dictionary. The next command allows us to parse this dictionary and save them to individual environment variables:

```
export fix_client_order_id=$(echo order_dict | jq -r '."last_client_order_id"')
export fix_order_id=$(echo order_dict | jq -r '."last_order_id"')
export fix_quantity=$(echo order_dict | jq -r '."last_quantity"')
export fix_side=$(echo order_dict | jq -r '."last_side"')
export fix_product_id=$(echo order_dict | jq -r '."last_product_id"')
```

Now, these variables are ready to be used in either of the following requests:

```
python client_cancel_order.py
```

Finally, you can modify an existing limit order by editing limit_price and quantity inside `build_modify_order.py` and running the following command:
```
python client_modify_order.py
```
