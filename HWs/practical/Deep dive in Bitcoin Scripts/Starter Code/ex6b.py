from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)

from ex1 import P2PKH_scriptPubKey
from ex6a import Q6a_txout_scriptPubKey
from ex6_values import *


def getSig(txin, txout, txin_scriptPubKey, pr_key):
    return create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, pr_key)


def Q6_scriptSig(txin, txout, txin_scriptPubKey):
    HamedSig = getSig(txin, txout, txin_scriptPubKey, Hamed_private_key)
    SaeedSig = getSig(txin, txout, txin_scriptPubKey, my_private_key)
    return [
        OP_0, HamedSig, SaeedSig
    ]


def send_from_Q6_transaction(amount_to_send, txid_to_spend, utxo_index,
                             txin_scriptPubKey, txout_scriptPubKey, network_type):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = Q6_scriptSig(txin, txout, txin_scriptPubKey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx, network_type)


######################################################################
if __name__ == '__main__':
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.00025   # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '7f6fbbf6f3ff531943ccf0f60043c770235df42fc25705653f62d1a78e40dee1')
    utxo_index = 0  # index of the output you are spending, indices start at 0

    ######################################################################
    txin_scriptPubKey = Q6a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_Q6_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)
