stadium_capacity = int(input())
fans_number = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(fans_number):
    fans_sector = input()
    if fans_sector == "A":
        sector_a += 1
    elif fans_sector == "B":
        sector_b += 1
    elif fans_sector == "V":
        sector_v += 1
    elif fans_sector == "G":
        sector_g += 1

sector_a_percent = sector_a / fans_number * 100
sector_b_percent = sector_b / fans_number * 100
sector_v_percent = sector_v / fans_number * 100
sector_g_percent = sector_g / fans_number * 100
total_fans_percent = fans_number / stadium_capacity * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{total_fans_percent:.2f}%")