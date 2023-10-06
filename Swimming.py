minutes_control = int(input())
seconds_control = int(input())
distance_to_swim = float(input())
seconds_per_100m = int(input())

control_time_seconds = (minutes_control * 60) + seconds_control

total_swim_time_seconds = (distance_to_swim / 100) * seconds_per_100m - ((distance_to_swim // 120) * 2.5)

if total_swim_time_seconds < control_time_seconds:
    print("Petar Mitsin won an Olympic quota!")
    print(f"His time is {total_swim_time_seconds:.3f}.")
else:
    time_difference = total_swim_time_seconds - control_time_seconds
    print(f"No, Petar failed! He was {abs(time_difference):.3f} second slower.")
