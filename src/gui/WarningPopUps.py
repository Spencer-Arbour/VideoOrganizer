from tkinter import messagebox


def use_app_directory(directory: str) -> bool:
    return messagebox.askokcancel(
        "Invalid Directory",
        "Cannot find the specified directory:\n'{}'\nWould you like to use the current directory instead?"
        .format(directory)
    )


def need_valid_directory(directory: str) -> None:
    messagebox.showinfo(
         "Invalid Directory",
         "Cannot find the specified{}directory. Please enter a valid one to proceed."
         .format(" " if directory == "" else "\n''" + directory + "'\n")
    )
