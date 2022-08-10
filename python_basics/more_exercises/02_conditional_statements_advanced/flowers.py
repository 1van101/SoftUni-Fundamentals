chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
day_type = input()

price_chrysanthemum = 0
price_roses = 0
price_tulips = 0
flowers_total = chrysanthemum_number + roses_number + tulips_number

if season == "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_roses = 4.10
    price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_roses = 4.50
    price_tulips = 4.15

bouquet_total = (price_chrysanthemum * chrysanthemum_number + price_roses * roses_number + price_tulips * tulips_number)

if day_type == "Y":
    bouquet_total *= 1.15
elif day_type == "N":
    bouquet_total

if season == "Spring" and tulips_number > 7:
    bouquet_total *= 0.95
if season == "Winter" and roses_number >= 10:
    bouquet_total *= 0.9
if flowers_total > 20:
    bouquet_total *= 0.8

bouquet_total_decorated = bouquet_total + 2
print(f"{bouquet_total_decorated:.2f}")
