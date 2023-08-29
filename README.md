# International Exchange (INTX) API Scripts

This repository provides Python examples of the Coinbase International Exchange Public APIs. These scripts are meant to be examples of minimally viable requests; therefore, logic is repeated between REST scripts to highlight what is necessary for any specific request, and FIX is designed to disconnect after each action.
# Getting started

## 1. Gaining access

Clone the repository with the following command:
```
git clone https://github.com/coinbase-samples/intx-scripts-py
```

## 2. Configuration

Depending on if you are accessing REST or FIX, dependencies will differ. Within each folder, you will find a requirements.txt file, from which you will be able to install dependencies with the following command: 

```
pip install -r requirements.txt
```

Additionally, these scripts make use of environment variables where applicable. Detailed READMEs for FIX and REST are provided in their respective directories. 
