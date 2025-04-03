from web3 import Web3
from web3.eth import Account
import json

# Charger les configurations depuis config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialiser la connexion Web3
web3 = Web3(Web3.HTTPProvider(config["ethereum_node_url"]))

if not web3.is_connected():
    raise ConnectionError("Impossible de se connecter au nœud Ethereum. Vérifiez l'URL du fournisseur.")

# Charger les informations nécessaires depuis le fichier de configuration
private_key = config["private_key"]
sender_address = config["sender_address"]
usdt_contract_address = config["usdt_contract_address"]
gas_price_gwei = config["gas_price_gwei"]
gas_limit = config["gas_limit"]

# Signature de la fonction ERC20 `transfer(address,uint256)`
usdt_transfer_signature = "0xa9059cbb"

def send_usdt_transaction(recipient_address, amount):
    """
    Envoie une transaction USDT (ERC-20) à un destinataire.
    :param recipient_address: Adresse Ethereum du destinataire.
    :param amount: Montant en USDT à envoyer (en unités entières, ex. 1 USDT = 1).
    """
    # Convertir le montant en wei (1 USDT = 10^6 wei pour USDT)
    amount_in_wei = int(amount * 10**6)

    # Récupérer le nonce pour l'adresse de l'expéditeur
    nonce = web3.eth.get_transaction_count(sender_address)

    # Construire les données pour l'appel de la fonction `transfer`
    data = (
        usdt_transfer_signature +
        recipient_address[2:].zfill(64) +
        hex(amount_in_wei)[2:].zfill(64)
    )

    # Construire la transaction
    transaction = {
        "to": usdt_contract_address,
        "value": 0,  # Les transactions ERC-20 n'envoient pas d'ETH
        "gasPrice": web3.to_wei(gas_price_gwei, "gwei"),
        "gas": gas_limit,
        "nonce": nonce,
        "data": data,
        "chainId": 1  # Mainnet Ethereum
    }

    # Signer la transaction avec la clé privée
    signed_tx = Account.sign_transaction(transaction, private_key)

    # Envoyer la transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction envoyée avec succès. Hash : {web3.to_hex(tx_hash)}")

    # Attendre la confirmation de la transaction
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if tx_receipt.status == 1:
        print("Transaction confirmée avec succès.")
    else:
        print("La transaction a échoué.")

# Exemple d'utilisation
if __name__ == "__main__":
    recipient = "0xRecipientAddressHere"  # Remplacez par l'adresse du destinataire
    amount_to_send = 1000000  # Montant en USDT (1 000 000 USDT dans cet exemple)
    send_usdt_transaction(recipient, amount_to_send)