lucky_numbers = [4, 7, 15, 16, 17]

friends = ["Kevin", "Gavin", "Rockey", "Erick"]


friends.extend(lucky_numbers)

friends.append("Creed")

friends.insert(1, "kelly")

friends.remove("Rockey")

lucky_numbers.reverse()

print(lucky_numbers)

friends2 = friends.copy()

print(friends2)
