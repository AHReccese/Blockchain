from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey

if __name__ == '__main__':
    ######################################################################
    # TODO(done): set these parameters correctly
    amount_to_send = 0.00005209 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
            '520be941ad9380e9e790099323f9fbd3db4d9cb690fb89b9204d68f7f561e345')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q2a_txout_scriptPubKey
    ######################################################################
    # TODO(done): implement the scriptSig for redeeming the transaction created
    # in  Exercise 2a.

    # a = 1635
    # b = 9610
    # 1635 <= 2000 - 100 = 1900 < 9610

    txin_scriptSig = [
            100,2000
    ]
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_custom_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)
