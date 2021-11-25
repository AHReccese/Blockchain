from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO(done): Complete the scriptPubKey implementation for Exercise 2

# studentID = 96101635
# a = min(9610,1635) = 1635
# b = max(9610,1635) = 9610

Q2a_txout_scriptPubKey = [
    OP_SUB, OP_ABS, 1635, 9610, OP_WITHIN
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO(done): set these parameters correctly
    amount_to_send = 0.00015209 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
