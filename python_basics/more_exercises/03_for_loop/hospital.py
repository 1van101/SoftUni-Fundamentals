period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range (1, period + 1):

    number_of_patients = int(input())

    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if number_of_patients <= doctors:
        treated_patients += number_of_patients
    else:
        untreated_patients += number_of_patients - doctors
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
