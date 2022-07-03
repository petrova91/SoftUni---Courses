class Party:
    def __init__(self):
        self.people = []


party = Party()

names = input()
total_people = 0
while not names == 'End':
    total_people += 1
    party.people.append(names)
    names = input()

print(f"Going: {', '.join(party.people)}")
print(f'Total: {total_people}')