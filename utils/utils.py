import os

def get_all_filepaths_from_path(basepath):
    f = []
    print("in1")
    for (dirpath, dirnames, filenames) in os.walk(basepath):
        print("in2")
        for filename in filenames:
            f.append(dirpath + "/" + filename)
    return f