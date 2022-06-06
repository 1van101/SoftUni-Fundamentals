record_seconds = float(input())
distance = float(input())
time_for_one_meter_seconds = float(input())

delay = distance // 15 * 12.5

time_to_swim_the_distance = distance * time_for_one_meter_seconds + delay
needed_seconds = time_to_swim_the_distance - record_seconds
if time_to_swim_the_distance < record_seconds:
    print (f"Yes, he succeeded! The new world record is {time_to_swim_the_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")