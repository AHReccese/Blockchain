from config import *
from bitcoin.core.script import *
from sys import exit
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from ex5a import txout_scriptPubKey
from ex5_values import *


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def getSig(txin, txout, txin_scriptPubKey, pr_key):
    return create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, pr_key)


def send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey, txout_scriptPubKey,
                                 network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)
    hamedSig = getSig(txin, txout, txin_scriptPubKey, Hamed_private_key)
    txin_scriptSig = [
        hamedSig, Hamed_public_key
    ]

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)
    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.0002  # amount of BTC in the output you're splitting minus fee

    txid_to_spend = (
        'f4dab2dd4e9a6f6d941387c88e74971967dafe1255742d5a03fe5dcb48c29125')

    utxo_index = 0  # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = txout_scriptPubKey
    ######################################################################
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_custom_transaction(
        amount_to_send, txid_to_spend,
        utxo_index, txin_scriptPubKey,
        txout_scriptPubKey, network_type)

    print(response.status_code, response.reason)
    print(response.text)
