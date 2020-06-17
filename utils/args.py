import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='SecureDrive - Encrypt/Decrypt Files on the go to keep your data secure.')
    parser.add_argument("-k", "--key", type=str, required=True, help="This will act as a key to decipher files")
    parser.add_argument("-p", "--path", type=str, required=True, help="Path of root dir for which you want to decipher/cipher all files")
    parser.add_argument("-m", "--mode", type=str, required=True, help="Set its value to D if Decipher, C if Cipher")
    return parser