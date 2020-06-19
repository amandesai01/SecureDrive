import os

def get_all_filepaths_from_path(basepath):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(basepath):
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    return f

def from_string_to_binary_string(basestring):
    return ''.join(format(ord(i), 'b') for i in basestring)

def keyify(basekey):
    '''
    Encryptor only accepts keys of size 32bit.
    So, we pad or reduce size of given key to adjust it to 32 bit frame.
    '''
    
    if len(basekey) == 32:
        return from_string_to_binary_string(basekey)
    elif len(basekey) < 32:
        req = 32 - len(basekey)
        return from_string_to_binary_string(basekey + 'k'*(32-len(basekey)))
    else:
        return from_string_to_binary_string(basekey[:32])