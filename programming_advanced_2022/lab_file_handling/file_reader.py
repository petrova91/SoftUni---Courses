with open("numbers.txt") as file:
    nums = [int(x) for x in file.read().split("\n")]
    sum_nums = sum(nums)
    print(sum_nums)