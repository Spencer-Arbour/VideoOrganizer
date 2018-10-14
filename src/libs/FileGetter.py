import os


def get_files(root_dir: str, extensions_to_filter_for: tuple="") -> "_get_files":
    if not os.path.isdir(root_dir):
        raise NotADirectoryError("Dir does not exist")

    return _get_files(root_dir, extensions_to_filter_for)


def _get_files(root_dir: str, extensions_to_filter_for: tuple="") -> tuple:

        for root, dirs, files in os.walk(root_dir):

            for file in files:

                if file.lower().endswith(extensions_to_filter_for):
                    yield root, file
