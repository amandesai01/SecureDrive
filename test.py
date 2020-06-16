from encryptor.Encryptor import Encryptor
from utils.utils import get_all_filepaths_from_path
from time import sleep

enc = Encryptor(b"k" * 16)

path = "/Users/aman/Desktop/SecureDrive/TestFolder"

files = get_all_filepaths_from_path(path)

for file in files:
    enc.encrypt_file(file)

print("Decrypting in 15 Seconds")

sleep(15)

for file in files:
    enc.decrypt_file(file + ".enc")