import re

pattern = r"%{1}(?P<customer>[A-Z]{1}[a-z]+)%([^\.\|%\$])*<{1}(?P<product>\w+)>{1}([^\.\|%\$])*\|{1}(?P<count>\d+)\|{1}([^\.\|%\$\d])*(?P<price>\d+(\.\d+)*)\$"
data_line = input()
total_income = 0
while not data_line == "end of shift":
    valid_order = re.match(pattern, data_line)
    if valid_order:
        read_info = [data.groupdict() for data in re.finditer(pattern, data_line)]
        total_price = int(read_info[0]["count"]) * float(read_info[0]["price"])
        total_income += total_price
        print(f'{(read_info[0]["customer"])}: {(read_info[0]["product"])} - {total_price:.2f}')
    data_line = input()
print(f"Total income: {total_income:.2f}")

