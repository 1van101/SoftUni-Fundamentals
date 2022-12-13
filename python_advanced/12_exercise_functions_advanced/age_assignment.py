def age_assignment(*args, **kwargs):
    result = ""

    for name in sorted(args):
        first_letter = name[0]
        result += f"{name} is {kwargs[first_letter]} years old." + "\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
