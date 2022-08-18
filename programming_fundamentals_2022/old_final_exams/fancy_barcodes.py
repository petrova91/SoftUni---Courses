import re

pattern_barcode = r"@#+([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})@#+"
pattern_digits = r"\d+"
count_barcodes = int(input())
for _ in range(count_barcodes):
    barcode = input()
    valid_barcode = re.findall(pattern_barcode, barcode)
    if len(valid_barcode) == 0:
        print("Invalid barcode")
    else:
        valid_barcode = "".join(valid_barcode)
        product_group = re.findall(pattern_digits, valid_barcode)
        if len(product_group) > 0:
            print(f'Product group: {"".join(product_group)}')
        else:
            print(f'Product group: 00')
