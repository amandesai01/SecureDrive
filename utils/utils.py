import os

def get_all_filepaths_from_path(basepath):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(basepath):
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    return f