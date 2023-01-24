def make_bold(func):
    def wrapper(*names):
        return "<b>" + func(*names) + "</b>"

    return wrapper


def make_italic(func):
    def wrapper(*names):
        return "<i>" + func(*names) + "</i>"

    return wrapper


def make_underline(func):
    def wrapper(*names):
        return "<u>" + func(*names) + "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
