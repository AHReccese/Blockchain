from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG
    ]
    ######################################################################


# forked from split_text_coins.py
def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txin = create_txin(txid_to_spend, utxo_index)
    txout = create_txout(amount_to_send / 3, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout] * 3)
    txin_scriptPubKey = sender_address.to_scriptPubKey()

    sighash = SignatureHash(txin_scriptPubKey, tx,0, SIGHASH_ALL)
    txin.scriptSig = CScript([sender_private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              sender_private_key.pub])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))

    return broadcast_transaction(tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00035209 - 0.00015 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '50384942bc525f515f49748082dcb4db05c26f2e0768513f57d202d2ccefb2cb')
    utxo_index = 25  # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(my_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
