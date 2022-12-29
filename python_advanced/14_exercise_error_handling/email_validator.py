import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def extract_info(email):
    matches = re.match(r"^(?P<user>[A-Za-z\d]+)@[a-z]+(?P<domain>[a-z.]+)$", email)
    if matches:
        matches = matches.groupdict()
    return matches


domains = [".org", ".com", ".bg", ".net"]

while True:
    line = input()

    if line == "End":
        break

    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    email_parts = extract_info(line)

    if len(email_parts['user']) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if email_parts['domain'] not in domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domains)}")

    print("Email is valid")


