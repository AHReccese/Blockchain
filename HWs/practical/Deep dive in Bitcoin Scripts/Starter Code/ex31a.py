from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import send_from_P2PKH_transaction
from ex3_values import *
######################################################################
# TODO(done): Complete the scriptPubKey implementation for Exercise 3

Q31a_txout_scriptPubKey = [
    OP_DEPTH, 1, OP_EQUAL, OP_IF, Faraz_public_key, # checking whether Faraz agrees on the transaction.
    OP_ELSE, 3, # checking whether Ata and 3 other shareholders agree on the transaction.
    sh1_public_key,
    sh2_public_key,
    sh3_public_key,
    sh4_public_key,
    sh5_public_key,
        5, OP_CHECKMULTISIGVERIFY, Ata_public_key, OP_ENDIF, OP_CHECKSIG
    ]
    ######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.00015  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q31a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
