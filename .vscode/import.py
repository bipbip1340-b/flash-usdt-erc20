import json

# Charger les configurations depuis config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Utiliser les configurations
web3 = Web3(Web3.HTTPProvider(config["ethereum_node_url"]))

if not web3.is_connected():
    raise ConnectionError("Failed to connect to the Ethereum node. Please check your HTTP provider URL.")

private_key = config["private_key"]
if not private_key:
    raise ValueError("Private key not found in the configuration file.")

sender_address = config["sender_address"]
usdt_contract_address = config["usdt_contract_address"]
gas_price_gwei = config["gas_price_gwei"]
gas_limit = config["gas_limit"]