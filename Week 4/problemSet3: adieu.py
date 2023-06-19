names = []

while True:
    try:
        user_input = input("Name: ").strip()
        if user_input != "Name: ":
            names.append(user_input)

    except EOFError:
        break

print("Adieu, adieu, to ", end="")
if len(names) > 2:
    for name in names[:-1]:
        print(name, end=", ")
    print("and", names[-1])
elif len(names) == 2:
    print(names[0], "and", names[1])
else:
    print(names[-1])
