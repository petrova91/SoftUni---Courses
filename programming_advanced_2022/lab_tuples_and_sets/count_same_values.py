numbers = input().split()
nums = {}

for digit in numbers:
    digit = float(digit)
    if digit not in nums:
        nums[digit] = 0
    nums[digit] += 1

for data in nums.items():
    print(f"{(data[0]):.1f} - {data[1]} times")
