count_rows = int(input())
total_nums = []

for _ in range(count_rows):
    nums = [int(x) for x in input().split(", ")]
    total_nums.extend(nums)

print(total_nums)