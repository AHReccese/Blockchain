from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress


def giveMePrivatePublicAddress(pr_key):
    private_key = CBitcoinSecret(pr_key)

    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)
    return private_key, public_key, address


Ata_private_key, Ata_public_key, Ata_address = giveMePrivatePublicAddress(
    'cQJ7dKepXM5AtKDqrMbm3hPaNJTCf7ki9iyrrn8Su2r7c8qZGCz3')
Faraz_private_key, Faraz_public_key, Faraz_address = giveMePrivatePublicAddress(
    'cUVgwKxGyds3m2h6v5VPhin7vRWQXp2HAoy92yHXeHzDvQtRAHBo')
sh1_private_key, sh1_public_key, sh1_address = giveMePrivatePublicAddress(
    'cQ4T7p66rM9PdKnAecqkNzhCeMs1CuDRBYqGWgQsaEjVHqinJJQv')
sh2_private_key, sh2_public_key, sh2_address = giveMePrivatePublicAddress(
    'cTgFpkc1DXmdguHXMQ99855cNvutWPqcMbCMQPXNwYZ5aq8wD92X')
sh3_private_key, sh3_public_key, sh3_address = giveMePrivatePublicAddress(
    'cRHeNQRMhxkAyYHrPM2wvvZkxhXaLfHBAhmSzf1a76fWD3G2pkjK')
sh4_private_key, sh4_public_key, sh4_address = giveMePrivatePublicAddress(
    'cVjv2FKr8RTX3CuwYWyAadtFQRnVqx5msn93aYAxH8wMVCSp8J1W')
sh5_private_key, sh5_public_key, sh5_address = giveMePrivatePublicAddress(
    'cQGgG48fg9APGeJ16ABi2CcX8hD6kLpukKZhJheAYHSmgKBNf51b')
