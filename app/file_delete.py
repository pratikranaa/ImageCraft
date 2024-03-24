import os
import glob
import shutil

def list_files_in_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            print(os.path.join(dirpath, filename))

def get_latest_file(directory_pattern):
    list_of_files = glob.glob(directory_pattern)
    if not list_of_files:  # If no files found
        return None
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    else:
        print(f"The directory {directory} does not exist")

