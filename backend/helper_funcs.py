import  os
import sys
from pathlib import Path

# FILE_PATH="../data/tasks.txt"

def get_app_data_path():
    """
    Determines where to save user data.
    In Dev: saves to the project's '../data/' directory.
    In Production (EXE): saves to a local 'data/' directory right next to the .exe file.
    """
    if getattr(sys, 'frozen', False):
        # Running as compiled EXE: get the directory where the .exe actually sits
        exe_dir = os.path.dirname(sys.executable)
        return os.path.normpath(os.path.join(exe_dir, "data"))
    else:
        # Running in development: get the script's parent project directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        return os.path.normpath(os.path.join(project_root, "data"))

# 1. Dynamically resolve the folder directory
DATA_DIR = get_app_data_path()
FILE_PATH = os.path.join(DATA_DIR, "tasks.txt")

# 2. Automatically generate the structure if it's a new installation
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file_local:
        pass  # Generates an empty tasks.txt file on initialization


def get_todos(file_path=FILE_PATH):
    """Reads the task file and returns to caller"""
    with open(file_path, "r") as file_local:
        todo_list_local=file_local.readlines()

    return todo_list_local

def write_todo(file_to_write, file_path=FILE_PATH):
    """Receives a data to write to a specified file"""
    with open(file_path, "w") as file_local:
        file_local.writelines(file_to_write)


if __name__ == "__main__":

    config_path=resource_path("../modules/helper_funcs.py")
    print(config_path)

