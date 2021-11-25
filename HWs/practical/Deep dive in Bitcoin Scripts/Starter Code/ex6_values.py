from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress


def giveMePrivatePublicAddress(pr_key):
    private_key = CBitcoinSecret(pr_key)
    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)
    return private_key, public_key, address


expiration_time = 1608057127  # at this time current time is : 1607057127
Hamed_private_key, Hamed_public_key, Hamed_address = giveMePrivatePublicAddress(
    'cQktcZu6tC9ZwBXp5ZnZHrPXuvbac9zPUgoRMFL74iBqKTitzmPB')
