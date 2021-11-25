from bitcoin.core.script import *


######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO(done): Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [OP_IF, OP_HASH160, hash_of_secret, OP_EQUALVERIFY, public_key_recipient, OP_CHECKSIG, OP_ELSE
        , OP_2, public_key_sender, public_key_recipient, OP_2, OP_CHECKMULTISIG, OP_ENDIF

            ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [sig_recipient, secret, OP_1
            ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [OP_0, sig_sender, sig_recipient, OP_0
            ]

######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO(done): Fill in all of these fields
#
## todo revise(not confimed)
alice_txid_to_spend = "4c86fb0a8c631327d9d44bbe3ac8a6c3a5d4d6d985ea5455bba24c86282daed5"
alice_utxo_index = 0
alice_amount_to_send = 0.0001

bob_txid_to_spend = "9977e06f90990512e0c90d1026ff2efa19418dabc7b4eec43466adc41f883eb4"
bob_utxo_index = 0
bob_amount_to_send = 0.0001

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height = 1896039

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height = 3155348

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = True

######################################################################
