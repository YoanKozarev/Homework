num_participants = int(input())

highest_score = -1
highest_score_name = ""

for _ in range(num_participants):
    name = input()
    total_points = 0

    while True:
        command = input()
        if command == "Stop":
            break
        points = int(command)
        total_points += points

    print(f"{name} has {total_points} points.")

    if total_points > highest_score:
        highest_score = total_points
        highest_score_name = name
        print(f"{name} is the new number 1!")

print(f"{highest_score_name} won competition with {highest_score} points!")
