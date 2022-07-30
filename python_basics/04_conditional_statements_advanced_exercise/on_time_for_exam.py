hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_arrival = minutes_of_arrival + hour_of_arrival * 60
time_of_exam = minutes_of_exam + hour_of_exam * 60

if time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print ("On time")
elif time_of_arrival < time_of_exam - 30:
    print("Early")
elif time_of_arrival > time_of_exam:
    print("Late")

difference = abs(time_of_arrival - time_of_exam)
difference_hours = difference // 60
difference_minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{difference_minutes} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    print(f"{difference_hours}:{difference_minutes:02d} hours before the start")
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f"{difference_minutes} minutes after the start")
elif time_of_arrival >= time_of_exam + 60:
    print(f"{difference_hours}:{difference_minutes:02d} hours after the start")

# time_of_exam_hours = int(input())
# time_of_exam_minutes = int(input())
# time_of_arrival_hours = int(input())
# time_of_arrival_minutes = int(input())
#
# exam_total_minutes = time_of_exam_minutes + (time_of_exam_hours * 60)
# arrival_total_minutes = time_of_arrival_minutes + (time_of_arrival_hours * 60)
#
# diff = abs(arrival_total_minutes - exam_total_minutes)
# diff_h = diff // 60
# diff_m = diff % 60
#
# if arrival_total_minutes > exam_total_minutes:
#     print("Late")
#     if exam_total_minutes < arrival_total_minutes < exam_total_minutes + 60:
#         print(f"{diff_m} minutes after the start")
#     elif arrival_total_minutes >= exam_total_minutes + 60:
#         print(f"{diff_h}:{diff_m:02d} hours after the start")
# elif exam_total_minutes - 30 <= arrival_total_minutes <= exam_total_minutes:
#     print("On time")
#     if exam_total_minutes != arrival_total_minutes:
#         print(f"{diff_m} minutes before the start")
# elif exam_total_minutes - 30 > arrival_total_minutes:
#     print("Early")
#     if exam_total_minutes - 60 < arrival_total_minutes < exam_total_minutes - 30:
#         print(f"{diff_m} minutes before the start")
#     elif exam_total_minutes - 60 >= arrival_total_minutes:
#         print(f"{diff_h}:{diff_m:02d} hours before the start")


