def lenght(usernames):
    if 3 <= len(usernames) <= 16:
        return True

def type_of_symbol(usernames):
    for char in usernames:
        if not(char.isalnum() or char == "_" or char == "-"):
            return False
    return True

def username_validation(usernames):
    if lenght(usernames) and type_of_symbol(usernames):
        return True


usernames_input = input().split(", ")
for username in usernames_input:
    if username_validation(username):
        print(username)