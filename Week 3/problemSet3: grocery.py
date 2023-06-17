list = {}
while True:
    try:
        user_input = input().upper()
        if user_input not in list:
            list[user_input] = 1
        else:
            list[user_input] += 1

    except EOFError:
        print()
        break

for item in sorted(list):
    print(list[item], item)
