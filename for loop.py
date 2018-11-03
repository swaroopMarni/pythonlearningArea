friends = ["jim", "keren", "keven"]

for friend in friends:
    print(friend)
print("\n")
for index in range(10):
    print(index)

for index in range(3,10):
    print(index)
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")

i = 1
while i < 6:
    print(i)
    if (i == 3):
        i += 1