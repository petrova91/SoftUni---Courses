def numbers_searching(*args):
    result = []
    repeated_nums = set()
    nums = set(args)
    min_num = min(args)
    max_num = max(args)
    full_sequence = set([x for x in range(min_num, max_num+1)])
    missing_num = list(full_sequence.difference(nums))
    result.extend(missing_num)
    for num in args:
        if args.count(num) > 1:
            repeated_nums.add(num)
    repeated_nums = list(repeated_nums)
    repeated_nums.sort()
    result.append(repeated_nums)
    return result


print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))