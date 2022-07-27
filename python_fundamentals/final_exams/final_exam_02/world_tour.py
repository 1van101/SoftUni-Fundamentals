def add_stop(stops, data):
    i = int(data[1])
    new_str = data[2]
    if 0 <= i < len(stops):
        left_side = stops[:i]
        right_side = stops[i:]
        stops = left_side + new_str + right_side
    return stops


def remove_stop(stops, data):
    start = int(data[1])
    end = int(data[2])
    if 0 <= start < len(stops) and 0 <= end < len(stops):
        stops = stops[:start] + stops[end + 1:]
    return stops


def switch(stops, data):
    old_str = data[1]
    new_str = data[2]
    if old_str in stops:
        stops = stops.replace(old_str, new_str)
    return stops


stops = input()
text = input()
while text != "Travel":
    current_text = text.split(":")
    action = current_text[0]
    if action == "Add Stop":
        stops = add_stop(stops, current_text)
    elif action == "Remove Stop":
        stops = remove_stop(stops, current_text)
    elif action == "Switch":
        stops = switch(stops, current_text)
    print(stops)

    text = input()

print(f"Ready for world tour! Planned stops: {stops}")
