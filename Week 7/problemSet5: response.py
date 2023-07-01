import validators

def main():
    print(valid(input("What's your email address? ")))


def valid(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
