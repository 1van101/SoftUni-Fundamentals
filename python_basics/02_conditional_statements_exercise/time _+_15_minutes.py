hours = int(input())
minutes = int(input())
minutes_total = minutes + 15
hours = hours + minutes_total//60
minutes = minutes_total % 60

if hours > 23:
    hours = 0
print (f"{hours}:{minutes:02d}")
