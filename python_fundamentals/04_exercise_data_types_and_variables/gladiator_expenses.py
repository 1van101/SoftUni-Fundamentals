lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = lost_fights_count // 2
sword_broken = lost_fights_count // 3
shield_broken = lost_fights_count // 6
armor_broken = lost_fights_count // 12

expenses_counter = helmet_broken * helmet_price + sword_broken * sword_price + shield_broken * shield_price + armor_broken * armor_price

print(f"Gladiator expenses: {expenses_counter:.2f} aureus")