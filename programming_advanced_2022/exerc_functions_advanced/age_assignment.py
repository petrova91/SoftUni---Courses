def age_assignment(*args, **kwargs):
    person_info = {}
    result = ""
    for current_name in args:
        letter = current_name[0]
        if letter in kwargs:
            person_info[current_name] = kwargs[letter]
    for name, age in sorted(person_info.items(), key=lambda x: x[0]):
        result += f"{name} is {age} years old." + "\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
