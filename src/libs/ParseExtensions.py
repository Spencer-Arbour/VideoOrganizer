def parse_extensions(given_extensions: str) -> tuple:
    broken_up_extensions = given_extensions.lower().replace(",", "").split(" ")

    for count, extension in enumerate(broken_up_extensions):
        if extension and extension[0] != ".":
            broken_up_extensions[count] = "." + extension

    return tuple(broken_up_extensions)