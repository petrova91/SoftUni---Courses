numbers = [int(x) for x in input().split()]
pos_num = []
neg_num = []

for num in numbers:
    if num > 0:
        pos_num.append(num)
    else:
        neg_num.append(num)

sum_neg_num = sum(neg_num)
sum_pos_num = sum(pos_num)

print(sum_neg_num)
print(sum_pos_num)
if abs(sum_neg_num) > sum_pos_num:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")