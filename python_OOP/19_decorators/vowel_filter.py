def vowel_filter(function):
    def wrapper():
        vowels = "aeoiuy"
        text = function()
        vowels_in_str = [x for x in text if x in vowels]
        return vowels_in_str

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
