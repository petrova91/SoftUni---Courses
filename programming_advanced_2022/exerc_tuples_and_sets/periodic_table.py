count_lines = int(input())

unique_elem = set()

for _ in range(count_lines):
    chemical_compounds = input().split()
    for elem in chemical_compounds:
        unique_elem.add(elem)

print("\n".join(unique_elem))