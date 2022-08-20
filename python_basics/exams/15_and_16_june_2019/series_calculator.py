name = input()
number_seasons = int(input())
number_episodes = int(input())
durations = float(input())

additional_time = number_seasons * 10
episode_with_ads = durations * 1.2
total_time = number_episodes * episode_with_ads * number_seasons + additional_time

print(f"Total time needed to watch the {name} series is {int(total_time)} minutes.")
