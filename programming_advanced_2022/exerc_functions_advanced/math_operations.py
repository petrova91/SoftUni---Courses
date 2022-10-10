def math_operations(*args, **kwargs):
    keys = [x for x in kwargs.keys()]
    counter = -1
    for num in args:
        counter += 1
        if counter == 4:
            counter = 0
        if keys[counter] == "a":
            kwargs[keys[counter]] += num
        elif keys[counter] == "s":
            kwargs[keys[counter]] -= num
        elif keys[counter] == "d":
            if num == 0:
                continue
            kwargs[keys[counter]] /= num
        elif keys[counter] == "m":
            kwargs[keys[counter]] *= num
    filter_result = [f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return "\n".join(filter_result)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
