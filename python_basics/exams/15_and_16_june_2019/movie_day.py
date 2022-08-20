time_for_record = int(input())
number_scenes = int(input())
duration_of_scene = int(input())


time_for_record_needed = duration_of_scene * number_scenes + (time_for_record * 0.15)
diff = abs(time_for_record_needed - time_for_record)
if time_for_record_needed > time_for_record:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
