from config import *
from bitcoin.core.script import *
from sys import exit
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from ex1 import send_from_P2PKH_transaction
from ex5_values import *

def P2PKH_scriptPubKey(address):
    ######################################################################
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################

txout_scriptPubKey = [

    timelock,  # time check(whether it is reached or not).
    OP_CHECKLOCKTIMEVERIFY,
    OP_DROP,

    OP_DUP,  # simple Hamed sigAuthen :)
    OP_HASH160,
    Hamed_address,
    OP_EQUALVERIFY,
    OP_CHECKSIG

]

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.0001  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    utxo_index = 19  # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txout_scriptPubKey, my_private_key, network_type)

    print(response.status_code, response.reason)
    print(response.text)
