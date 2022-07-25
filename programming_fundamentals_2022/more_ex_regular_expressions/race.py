import re

pattern_name = r"(?P<name>[A-Za-z])"
pattern_digit = r"(?P<num>\d)"
participants = input().split(", ")
racers = {}
information = input()
while not information == "end of race":
    racer_name = "".join(re.findall(pattern_name, information))
    digits = re.findall(pattern_digit, information)
    sum_digits = sum([int(num) for num in digits])
    if racer_name in participants:
        if racer_name not in racers:
            racers[racer_name] = 0
        racers[racer_name] += sum_digits
    information = input()

sort_racer = sorted(racers.items(), key=lambda x: -x[1])
print(f"1st place: {sort_racer[0][0]}")
print(f"2nd place: {sort_racer[1][0]}")
print(f"3rd place: {sort_racer[2][0]}")

