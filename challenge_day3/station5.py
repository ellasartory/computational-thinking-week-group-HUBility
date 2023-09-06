def solution_station_5(member_name, team_data):
    for team_number, team_members in team_data.items():
        if member_name in team_members:
            return team_number
    return None

# Sample team data
teams = {
    1: ["Mika", "Maria", "Isis", "Rosa", "Maja", "Damaris"],
    2: ["Emily", "Celia", "Carine", "Sabrina", "Gur"],
    3: ["Elisa", "Sari", "Dave", "Dima", "Jesper", "Martyna"],
    4: ["Kelt", "Sebastian", "Quanpu", "Ruben", "Sofia", "Gabriella"],
    5: ["Kian", "Sahir", "Tom", "Gonzalo", "Ameer", "Teun"],
    6: ["Angelica", "Matas", "Caleb", "Angeline", "Raven", "Paulina"],
    7: ["Mate", "Vincent", "Eryk", "Emma"],
    8: ["Hielke", "Liss", "Beatris", "Caio", "Sally", "Sanne"],
    9: ["Atlas", "Elli", "Felix", "Diana", "Yash"],
    10: ["Akanksha", "Charlie", "Andrey", "Max", "Hugo", "Al-fatihi"],
    11: ["Misha", "Ioanna", "Ella", "Cristian", "Alicja", "Vanessa"],
    12: ["Luca", "Rachna", "Jelle", "Karolina", "Yuyue", "Alexia"],
    # Add more teams as needed
}

# Ask for a member's name and find their team number
member_name = input("Name:")
team_number = solution_station_5(member_name, teams)

print(team_number)
