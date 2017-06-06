import os


def get_prank_files():
    actual_path = os.path.dirname(os.path.abspath(__file__))
    photos_path = r"%s\resources\prank" % actual_path
    return os.listdir(photos_path), photos_path


def rename_files(files, files_path):
    actual_path = os.getcwd()
    os.chdir(files_path)
    translate_table = str.maketrans(dict.fromkeys("0123456789"))
    for file in files:
        os.rename(file, file.translate(translate_table))
    os.chdir(actual_path)

photos, path = get_prank_files()
rename_files(photos, path)
