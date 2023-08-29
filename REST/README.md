# International Exchange API REST Scripts

This repository provides examples of common [REST API endpoints](https://docs.cloud.coinbase.com/intx/reference) to use with Coinbase International Exchange (INTX).
# Getting started

## 1. Gaining access

Clone the repository with the following command:
```
git clone https://github.com/coinbase-samples/intx-scripts-py
```

## 2. Configuration

Within the REST folder, you will find a requirements.txt file, from which you will be able to install dependencies with the following command: 

```
pip install -r requirements.txt
```

Additionally, these scripts make use of environment variables where applicable. 

To fill these values, you will need to generate an API key with trading and reading functionality. Populate the below and run the following to declare these variables:

```bash

export ACCESS_KEY=ACCESSKEYHERE
export PASSPHRASE=PASSPHRASEHERE
export SIGNING_KEY=SIGNING_KEYHERE
```

## 3. Running scripts

Run directly from your command line, e.g.: 
```
python intx_list_portfolios.py
```

Several of these scripts utilize command line arguments to increase ease of use, e.g.:
```
python intx_get_order_details.py <portfolio> <id>
```