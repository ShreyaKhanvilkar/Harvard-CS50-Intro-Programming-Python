def main():
    user_input = value(input("Greeting: ").lower())
    print(user_input)


def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
