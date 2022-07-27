def cast_spell(heroes, name, mp_needed, spell_name):
    if heroes[name]["mana"] >= mp_needed:
        heroes[name]["mana"] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mana']} MP!")
    else:
        print(f'{name} does not have enough MP to cast {spell_name}!')
    return heroes


def take_damage(heroes, name, dmg, attacker):
    if heroes[name]["health"] > dmg:
        heroes[name]["health"] -= dmg
        print(f"{name} was hit for {dmg} HP by {attacker} and now has {heroes[name]['health']} HP left!")
    else:
        del heroes[name]
        print(f"{name} has been killed by {attacker}!")
    return heroes


def recharge(heroes, name, amount):
    if heroes[name]["mana"] + amount > 200:
        print(f"{name} recharged for {200 - heroes[name]['mana']} MP!")
        heroes[name]["mana"] = 200
    else:
        heroes[name]["mana"] += amount
        print(f"{name} recharged for {amount} MP!")
    return heroes


def heal(heroes, name, amount):
    if heroes[name]["health"] + amount > 100:
        print(f"{name} healed for {100 - heroes[name]['health']} HP!")
        heroes[name]["health"] = 100
    else:
        heroes[name]["health"] += amount
        print(f"{name} healed for {amount} HP!")
    return heroes


number_of_heroes = int(input())

heroes_and_data = {}

for hero in range(number_of_heroes):
    name, hp, mp = input().split()
    heroes_and_data[name] = {"health": int(hp), "mana": int(mp)}

command = input()
while not command == "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        current_name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        heroes_and_data = cast_spell(heroes_and_data, current_name, mana_needed, spell_name)
    elif action == "TakeDamage":
        current_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_and_data = take_damage(heroes_and_data, current_name, damage, attacker)
    elif action == "Recharge":
        current_name = command[1]
        amount = int(command[2])
        heroes_and_data = recharge(heroes_and_data, current_name, amount)
    elif action == "Heal":
        current_name = command[1]
        amount = int(command[2])
        heroes_and_data = heal(heroes_and_data, current_name, amount)

    command = input()

for key in heroes_and_data.keys():
    print(f"{key}\n  HP: {heroes_and_data[key]['health']}\n  MP: {heroes_and_data[key]['mana']}")
