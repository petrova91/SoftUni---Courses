count_guests = int(input())

guests = set()

for _ in range(count_guests):
    guest_code = input()
    guests.add(guest_code)

code = input()
while not code == "END":
    guests.discard(code)
    code = input()

print(len(guests))
print("\n".join(sorted(guests)))