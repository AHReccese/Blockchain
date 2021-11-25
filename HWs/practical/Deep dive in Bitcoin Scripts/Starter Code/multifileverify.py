import hashlib
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import *
from ex1 import send_from_P2PKH_transaction
from merkle_tree import rootCalculater
from bitcoin.core.script import *

def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    return [signature, my_public_key]
    ######################################################################

if __name__ == '__main__':
    ######################################################################

    SelectParams('testnet')
    numberoffiles = 14
    merkleroot = rootCalculater(numberoffiles)

    seckey = CBitcoinSecret.from_secret_bytes(x(merkleroot))
    address = P2PKHBitcoinAddress.from_pubkey(seckey.pub)

    ##
    your_address = address
    amount_to_send = 0.00035209 - 0.00015
    txid_to_spend = (
        '50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    # second tx id  'fb549c431a5d3b8fe4ef67bb21625b0c468bf55dc75305fcee7176574603962c'
    utxo_index = 16
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(your_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
