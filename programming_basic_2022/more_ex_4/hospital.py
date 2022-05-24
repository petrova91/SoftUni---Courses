period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for days in range(1, period + 1):
    count_patients = int(input())
    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if count_patients <= doctors:
        treated_patients += count_patients
    else:
        treated_patients += doctors
        untreated_patients += count_patients - doctors
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
