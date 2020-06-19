import os

def get_all_filepaths_from_path(basepath):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(basepath):
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    return f

def keyify(basekey):
    '''
    Encryptor only accepts keys of size 32bit.
    So, we pad or reduce size of given key to adjust it to 32 bit frame.
    '''

    if len(basekey) == 32:
        return basekey
    elif len(basekey) < 32:
        return basekey + 'k'*(32-len(basekey))
    else:
        return basekey[:32]