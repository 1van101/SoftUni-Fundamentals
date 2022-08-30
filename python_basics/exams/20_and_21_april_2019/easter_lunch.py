easter_bread_num = int(input())
eggshell_num = int(input())
cookies_kg = int(input())
eggs_num = 12 * eggshell_num
total_price = easter_bread_num * 3.20 + eggshell_num * 4.35 + cookies_kg * 5.40 + eggs_num * 0.15
print(f"{total_price:.2f}")