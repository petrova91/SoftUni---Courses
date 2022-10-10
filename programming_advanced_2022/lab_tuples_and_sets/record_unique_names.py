count_names = int(input())
names = set()

for _ in range(count_names):
    name = input()
    names.add(name)

print("\n".join(names))