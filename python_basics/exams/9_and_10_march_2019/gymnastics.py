country = input()
device = input()
points = 0
max_points = 20
if country == "Russia":
    if device == "ribbon":
        points = 9.1 + 9.4
    elif device == "hoop":
        points = 9.3 + 9.8
    else:
        points = 9.6 + 9
elif country == "Bulgaria":
    if device == "ribbon":
        points = 9.6 + 9.4
    elif device == "hoop":
        points = 9.55 + 9.75
    else:
        points = 9.5 + 9.4
else:
    if device == "ribbon":
        points = 9.2 + 9.5
    elif device == "hoop":
        points = 9.45 + 9.35
    else:
        points = 9.7 + 9.15
diff_percent = (max_points - points) / max_points * 100
print(f"The team of {country} get {points:.3f} on {device}.")
print(f"{diff_percent:.2f}%")
