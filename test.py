from encryptor.Encryptor import Encryptor
from utils.utils import get_all_filepaths_from_path
from time import sleep

enc = Encryptor(b"k" * 32)

TIMEOUT = 2

path = "/Users/aman/Desktop/SecureDrive/TestFolder"

files = get_all_filepaths_from_path(path)

for file in files:
    enc.encrypt_file(file)

print("Decrypting in {} Seconds".format(TIMEOUT))

sleep(TIMEOUT)

for file in files:
    enc.decrypt_file(file + ".enc")