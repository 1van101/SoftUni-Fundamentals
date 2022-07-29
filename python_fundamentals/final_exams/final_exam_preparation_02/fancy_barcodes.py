import re


def print_barcode_group(barcode):
    match = re.search(r"@#+([A-Z][A-Za-z\d]{4,}[A-Z])@#+", barcode)
    if match:
        digit = re.findall(r"\d", match.group(1))
        if digit:
            print(f"Product group: {''.join(digit)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")


num_of_barcodes = int(input())
for i in range(num_of_barcodes):
    current_barcode = input()
    print_barcode_group(current_barcode)