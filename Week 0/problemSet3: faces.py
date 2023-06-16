user_input = input("Enter your input: ")

def convert(x):
        return x.replace(":(", "🙁").replace(":)", "🙂")

def main():
    print(convert(user_input))

main()
