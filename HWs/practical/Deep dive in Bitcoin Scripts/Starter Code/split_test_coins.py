from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC,
    bob_secret_key_BTC, bob_public_key_BTC, bob_address_BTC,
    alice_secret_key_BCY, alice_public_key_BCY, alice_address_BCY,
    bob_secret_key_BCY, bob_public_key_BCY, bob_address_BCY,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction

def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO(done): set these parameters correctly

    # for me
    # private_key = CBitcoinSecret(
    # 'cMkGiqUJ5jt7TxEnhGK5FSj2vEfSyaGoJd6WugbnRsdNvBVVenAz')
    # txid_to_spend : 514808fa3dd0c861f5b82dd4a9972d170b7072bda63b16dafcbcac6989a20976
    # utxo_index = 0
    # amount = 0.01878155 BTC

    # for Alice
    private_key = CBitcoinSecret(
    'cTLEKgMEXuFN8DbNm47vRnkSZjm59dpJzJ8L1hWpLYBLuXFpfgoH')
    # txid_to_spend : 3846dee3da60128135bd3c46795dae8afb2b4314ed921022ec7376d283f9acd1
    # utxo_index = 1
    # amount = 0.01509217 BTC

    # for Bob
    # private_key = CBitcoinSecret.from_secret_bytes(
    #    x('98ff391c7f2fbda18d9329083a490685ae0a2db63438c637c5c2fd5470359fca'))

    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    amount_to_send = 0.01026283 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '3846dee3da60128135bd3c46795dae8afb2b4314ed921022ec7376d283f9acd1')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    n = 30 # number of outputs to split the input into
    # For n, choose a number larger than what you immediately need,
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)
