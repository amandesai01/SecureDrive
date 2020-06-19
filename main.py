from utils.utils import get_all_filepaths_from_path, keyify
from utils.args import get_parser
from encryptor.Encryptor import Encryptor

parser = get_parser()
args = parser.parse_args()

filepaths = get_all_filepaths_from_path(args.path)

enc = Encryptor(keyify(args.key))

if args.mode == 'C':
    '''
    In case, there is error while encrypting a file,
    all files will be reverted back to orignal state.
    '''
    encrypteds = []
    try:
        for path in filepaths:
            enc.encrypt_file(path)
            encrypteds.append(path)
    except Exception as e:
        print(e)
    else:
        print("Encrypted Successfully.")

elif args.mode == 'D':
    try:
        for path in filepaths:
            enc.decrypt_file(path)
    except Exception as e:
        print(e)
    else:
        print("Decrypted Successfully.")