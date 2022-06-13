def password_len(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def password_content(password):
    if password.isalnum():
        return True
    return False


def password_digits(password):
    counter = 0
    for i in password:
        if i.isdigit():
            counter += 1
    if counter < 2:
        return False
    return True


password_input = input()

len_of_password = password_len(password_input)
content_of_password = password_content(password_input)
digits_in_password = password_digits(password_input)

if not len_of_password:
    print("Password must be between 6 and 10 characters")
if not content_of_password:
    print("Password must consist only of letters and digits")
if not digits_in_password:
    print("Password must have at least 2 digits")
if len_of_password and content_of_password and digits_in_password:
    print("Password is valid")
