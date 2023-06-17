def main():
    user_input = get_int("Fraction: ")
    print(user_input)


def get_int(prompt):
    while True:
        try:
            x,y = input(prompt).split("/")
            tank = int(x) / int(y)
            if 0 <= tank <= 0.1:
                return "E"
            elif 0.9 <= tank <= 1:
                return "F"
            elif 0.1 < tank < 0.9:
                return str(round(tank*100)) + "%"

        except (ValueError,ZeroDivisionError):
            pass


main()
