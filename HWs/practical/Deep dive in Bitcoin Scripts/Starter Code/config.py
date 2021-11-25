from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

###
# keyGen for me
# Private key: cMkGiqUJ5jt7TxEnhGK5FSj2vEfSyaGoJd6WugbnRsdNvBVVenAz
# Address: mhWk598SxE7mdtVknX7YRmgjvEydF5ruq6
###

my_private_key = CBitcoinSecret(
    'cMkGiqUJ5jt7TxEnhGK5FSj2vEfSyaGoJd6WugbnRsdNvBVVenAz')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################


######################################################################
# NOTE: This section is for Question 10
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
# Private key: cTLEKgMEXuFN8DbNm47vRnkSZjm59dpJzJ8L1hWpLYBLuXFpfgoH
# Address: mweovmDWQgZXHUnKW56EVHDiUfcHKePsH3
alice_secret_key_BTC = CBitcoinSecret(
    'cTLEKgMEXuFN8DbNm47vRnkSZjm59dpJzJ8L1hWpLYBLuXFpfgoH')


# Only to be imported by bob.py
###
# keyGen for Bob
# Private key: cMuffQH2jc6zuUEbeJXdJfYF7DVA7izBxAQjNFfr67vut2XtfcRj
# Address: mqj24fphwtNZXfBzBtLPWwVy6Akgv6uDXA
###
bob_secret_key_BTC = CBitcoinSecret(
    'cMuffQH2jc6zuUEbeJXdJfYF7DVA7izBxAQjNFfr67vut2XtfcRj')

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 10
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('64e9a00742176378cd2b1a9f3c83949658824d858758a2f64edfb1030c356def'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('98ff391c7f2fbda18d9329083a490685ae0a2db63438c637c5c2fd5470359fca'))

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
