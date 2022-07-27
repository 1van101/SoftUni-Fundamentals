import re

number_of_barcodes = int(input())
barcodes = []
for code in range(number_of_barcodes):
    barcodes.append(input())

matches = re.finditer(r"([@][#]+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])([@][#]+)", ' '.join(barcodes))

valid_barcodes = [x.group("barcode") for x in matches]

for barcode in barcodes:
    is_valid = False
    for valid_barcode in valid_barcodes:
        if valid_barcode in barcode:
            is_valid = True
            break

    if is_valid:
        digits = re.findall(r"[0-9]", barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")

