import re

purchase_info = input()
total_cost = 0
pattern = r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
valid_purchase = []
while not purchase_info == "Purchase":
    check_purchase = re.match(pattern, purchase_info)
    if check_purchase:
        valid_purchase.append(check_purchase.groupdict())
    purchase_info = input()
print("Bought furniture:")
for current_item in valid_purchase:
    print(f'{current_item["furniture_name"]}')
    total_cost += float(current_item["price"]) * int(current_item["quantity"])
print(f"Total money spend: {total_cost:.2f}")
