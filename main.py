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
    except:
        for path in encrypteds:
            enc.decrypt_file(path)