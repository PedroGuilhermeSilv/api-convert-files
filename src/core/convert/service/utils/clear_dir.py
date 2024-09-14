import os


def clear_dir()-> bool:
    old_files = os.listdir("src/infra/convert/tmp/")
    for old_file in old_files:
        os.remove(os.path.join("src/infra/convert/tmp/", old_file))
    return True