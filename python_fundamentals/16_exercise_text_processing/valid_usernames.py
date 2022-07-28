def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_content(name):
    for ch in name:
        if not ch.isalnum() and not ch == "-" and not ch == "_":
            return False
    return True


def user_is_valid(name):
    if valid_length(name) and valid_content(name):
        return True
    return False


usernames = input().split(", ")

for user in usernames:
    if user_is_valid(user):
        print(user)


#__________________________________________
# import re
#
# text = input()
# matches = re.findall(r"(?:(?<=^)|(?<=, ))([\w\-]{3,16})(?:(?=$)|(?=,))", text)
#
# [print(x) for x in matches]

