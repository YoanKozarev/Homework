import math

series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_duration = int(input())


total_duration_in_minutes = (number_of_seasons * (number_of_episodes * episode_duration)) + (number_of_seasons * 0.25 * number_of_episodes * episode_duration) + (number_of_seasons * 12)

total_duration_in_minutes = math.floor(total_duration_in_minutes)

print(f"I needed {total_duration_in_minutes} minutes to watch the {series_name} all series.")
