from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO(done): Complete the scriptPubKey implementation for Exercise 2

save_message_scriptPubKey = [
    OP_RETURN,str.encode("Rostami96101635")
]

######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO(done): set these parameters correctly
    amount_to_send = 0.00035209 - 0.00015 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    utxo_index = 5 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        save_message_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
