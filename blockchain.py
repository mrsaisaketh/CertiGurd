from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Your deployed contract address
contract_address = Web3.to_checksum_address(
    "0xac075712EE530cb4b0ECa321C494a058Fa18641C"
)

# Contract ABI (paste from Remix after compilation → ABI section)
contract_abi = [
    {
        "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}],
        "name": "storeCertificateHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}],
        "name": "verifyCertificateHash",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Use first Ganache account
account = w3.eth.accounts[0]

def store_hash(cert_hash_hex):
    return True

def verify_hash(cert_hash_hex):
    return True