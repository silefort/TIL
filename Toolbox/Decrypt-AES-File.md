# Decrypt an AES encrypted file

Here is a quick script to decrypt jrnl files:

    #!/usr/bin/env python3

    import argparse
    from Crypto.Cipher import AES
    import getpass
    import hashlib
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="journal file to decrypt")
    args = parser.parse_args()

    pwd = getpass.getpass()
    key = hashlib.sha256(pwd.encode('utf-8')).digest()

    with open(args.filepath, 'rb') as f:
        ciphertext = f.read()

        crypto = AES.new(key, AES.MODE_CBC, ciphertext[:16])
        plain = crypto.decrypt(ciphertext[16:])
        plain = plain.strip(plain[-1:])
        plain = plain.decode("utf-8")
        print(plain)

This piece of code was stolen from here: https://jrnl.sh/encryption/
