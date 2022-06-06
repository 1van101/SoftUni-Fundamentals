time_first = int(input())
time_second = int(input())
time_third = int(input())
time_all = time_first + time_second + time_third
minutes = time_all // 60
seconds = time_all % 60
print (f"{minutes}:{seconds:02d}")