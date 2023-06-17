user_input = input("camelCase: ")

snake = ""

for i in user_input:
    if i.islower():
        snake += i
    if i.isupper():
        snake += "_" + i.lower()

print(snake)
