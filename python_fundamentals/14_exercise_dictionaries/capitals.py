countries = input().split(", ")
capitals = input().split(", ")
country_and_capital = {print(f"{x} -> {y}") for x, y in zip(countries, capitals)}

