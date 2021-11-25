from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,faucet_address, network_type)

from ex1 import P2PKH_scriptPubKey
from ex32a import Q32a_txout_scriptPubKey
from ex3_values import *


def getSig(txin, txout, txin_scriptPubKey, pr_key):
    return create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, pr_key)

def Q32_scriptSig(txin, txout, txin_scriptPubKey):
    Faraz_sig = getSig(txin, txout, txin_scriptPubKey, Faraz_private_key)
    Ata_sig = getSig(txin, txout, txin_scriptPubKey, Ata_private_key)
    sh1_sig = getSig(txin, txout, txin_scriptPubKey, sh1_private_key)
    sh2_sig = getSig(txin, txout, txin_scriptPubKey, sh2_private_key)
    sh3_sig = getSig(txin, txout, txin_scriptPubKey, sh3_private_key)
    sh4_sig = getSig(txin, txout, txin_scriptPubKey, sh4_private_key)
    sh5_sig = getSig(txin, txout, txin_scriptPubKey, sh5_private_key)

    # sample for second condition:
    # Either Faraz or Ata and 3 other shareholders agree on the transaction.
    return [
        OP_0, Faraz_sig, OP_0, sh1_sig, sh2_sig,sh5_sig
    ]

def send_from_Q32_transaction(amount_to_send, txid_to_spend, utxo_index,txin_scriptPubKey, txout_scriptPubKey, network_type):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = Q32_scriptSig(txin, txout, txin_scriptPubKey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,txin_scriptSig)
    return broadcast_transaction(new_tx, network_type)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.00025  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('30aaf92e1fe9160942d39f266493b146bd10aaab05ff98a3665c7931409076b7')
    utxo_index = 0  # index of the output you are spending, indices start at 0

    ######################################################################
    txin_scriptPubKey = Q32a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_Q32_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)
