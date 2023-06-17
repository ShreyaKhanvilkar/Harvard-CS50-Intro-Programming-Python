user_input = input("Input: ")

text = ""

for i in user_input:
    match i.lower():
        case "a" | "e" | "i" | "o" | "u":
            text += ""
        case _:
            text += i

print(text)
