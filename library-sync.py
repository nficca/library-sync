import sys
import os
import shutil
import pathlib

# Verify correct arguments given
if len(sys.argv) != 3 or not (os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
    print("Must specify two directories to synchronize")
    exit(0)

master = sys.argv[1]
copy = sys.argv[2]

join = os.path.join

def pretty_print_path(msg, path):
    """prints a msg along with a nicer representation of the path given"""
    print(msg + str(pathlib.Path(*pathlib.Path(path).parts[1:])), flush=True)

def ls(directory, indent=0):
    """neatly lists ALL files in directory (includes files in every sub-directory)"""
    for item in os.listdir(directory):
        print(("{0:>" + str(indent * 2 + len(item)) + "}").format(item))
        if os.path.isdir(join(directory, item)):
            ls(join(directory, item), indent + 1)

def sync(src, dest):
    """synchronizes all files from src to dest such that dest should contain the same files as src"""

    # iterate over source directory
    for item in os.listdir(src):
        # check if item is directory
        if os.path.isdir(join(src, item)):
            # check if same directory exists for dest
            if os.path.isdir(join(dest, item)):
                # sync the two sub directories
                sync(join(src, item), join(dest, item))
            # directory is not in dest so copy it over
            else:
                pretty_print_path("Copying all of ", join(src, item))
                shutil.copytree(join(src, item), join(dest, item))
        # not a directory so it's a file
        else:
            # check if file exists in dest
            if os.path.isfile(join(dest, item)):
                # compare modified dates
                src_time = os.path.getmtime(join(src, item))
                dest_time = os.path.getmtime(join(dest, item))
                if (dest_time != src_time):
                    # if modified dates are not the same, overwrite the file in dest with the one in src
                    pretty_print_path("Overwriting ", join(dest, item))
                    os.remove(join(dest, item))
                    shutil.copy2(join(src, item), dest)

            # file does not exist in dest so copy it over
            else:
                pretty_print_path("Copying ", join(src, item))
                shutil.copy2(join(src, item), dest)

    # iterate over destination directory
    for item in os.listdir(dest):
        # check if item is not in source
        if item not in os.listdir(src):
            # remove the entire directory or file if it is not in source
            if os.path.isdir(join(dest, item)):
                pretty_print_path("Removing all of ", join(dest, item))
                shutil.rmtree(join(dest, item))
            else:
                pretty_print_path("Removing ", join(dest, item))
                os.remove(join(dest, item))

# synchronize master and copy
sync(master, copy)