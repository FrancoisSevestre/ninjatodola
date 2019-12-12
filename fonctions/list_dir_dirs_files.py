from os import listdir, path

def list_dir_dirs_files(path_to_file):
    """Reads the path location and returns a tuple of dirs and files contained in it."""
    files = [f for f in listdir(path_to_file) if path.isfile(path.join(path_to_file, f))]
    dirs = [d for d in listdir(path_to_file) if path.isdir(path.join(path_to_file, d))]
    output = (dirs, files)
    return output

