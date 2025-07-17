n = int(input("Enter number of teams: "))
teams = []
for i in range(n):
    a = input(f"Enter team {i+1} name: ")
    teams.append(a)
meet = int(input("Enter number of meetings between one pair: "))
match = []
for i in range(n-1):
    for j in range(i+1, n):
        for k in range(meet):
            match.append((teams[i], teams[j]))
print("------------")
for idx, (team1, team2) in enumerate(match, 1):
    print(f"{idx}. {team1} vs {team2}")