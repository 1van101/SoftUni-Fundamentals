dwarf_dct = {}
hat_counter = {}
command = input()

while not command == "Once upon a time":
    dwarf_name, hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    dwarf_data = f"{hat_color}:{dwarf_name}"
    if dwarf_data not in dwarf_dct:
        dwarf_dct[dwarf_data] = [dwarf_physics, hat_color]
        if hat_color not in hat_counter:
            hat_counter[hat_color] = 0
        hat_counter[hat_color] += 1
    if dwarf_dct[dwarf_data][0] < dwarf_physics:
        dwarf_dct[dwarf_data][0] = dwarf_physics

    command = input()

dwarf_dct_sorted = dict(sorted(dwarf_dct.items(), key=lambda kv: (kv[1][0], hat_counter[kv[1][1]]), reverse=True))


for data, points in dwarf_dct_sorted.items():
    color, name = data.split(":")
    physics = points[0]
    print(f"({color}) {name} <-> {physics}")
