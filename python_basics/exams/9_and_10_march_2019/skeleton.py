minutes_needed = int(input())
seconds_needed = int(input())
lenght = float(input())
seconds_for_hundred_meters = int(input())
time_in_seconds_needed = minutes_needed * 60 + seconds_needed
delay = lenght / 120 * 2.5
total_time = (lenght / 100) * seconds_for_hundred_meters - delay
diff = abs(total_time - time_in_seconds_needed)
if total_time <= time_in_seconds_needed:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")