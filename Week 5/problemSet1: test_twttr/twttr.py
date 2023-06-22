def main():
    user_input = shorten(input("Input: "))
    print(user_input)


def shorten(word):
    text = ""
    for i in word:
        match i.lower():
            case "a" | "e" | "i" | "o" | "u":
                text += ""
            case _:
                text += i
    return text


if __name__ == "__main__":
    main()
