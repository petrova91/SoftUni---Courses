count_lines = int(input())

odd_nums = set()
even_nums = set()

for row in range(1, count_lines+1):
    name = input()
    name_ascii_code = sum([ord(sym) for sym in name]) // row
    if name_ascii_code % 2 == 0:
        even_nums.add(name_ascii_code)
    else:
        odd_nums.add(name_ascii_code)

sum_even = sum(even_nums)
sum_odd = sum(odd_nums)

if sum_odd == sum_even:
    result = odd_nums.union(even_nums)
elif sum_odd > sum_even:
    result = odd_nums.difference(even_nums)
else:
    result = odd_nums.symmetric_difference(even_nums)
print(*result, sep=", ")


