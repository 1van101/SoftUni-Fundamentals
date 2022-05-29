def grades_in_string(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.99:
        return "Poor"
    elif 3.5 <= grade <= 4.49:
        return "Good"
    elif 4.5 <= grade <= 5.49:
        return "Very Good"
    elif 5.5 <= grade <= 6:
        return "Excellent"


grade_data = float(input())

print(grades_in_string(grade_data))
