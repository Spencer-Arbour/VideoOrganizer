import os


def is_there_entered_value_that_is_directory(directory: str) -> bool:
    return os.path.isdir(directory) or directory == ""


# will not test as it would essentially test os.path.isdir
def is_directory_exist(directory: str) -> bool:
    return os.path.isdir(directory)
