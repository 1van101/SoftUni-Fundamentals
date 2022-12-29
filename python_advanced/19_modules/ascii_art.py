from pyfiglet import figlet_format as fm


def ascii_art(text):
    return fm(text)


print(ascii_art(input()))