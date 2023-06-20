from random import randint


def main():
    level = get_level()
    quest = 10
    correct = 0
    tries = 3
    while quest > 0:
        if tries == 3:
            problem = str(generate_integer(level)) + " + " + str(generate_integer(level))
            while tries > 0:
                try:
                    answer = int(input(problem + " = "))
                    if answer == eval(problem):
                        quest -= 1
                        correct += 1
                        tries = 3
                        break
                    else:
                        tries -= 1
                        raise ValueError
                except ValueError:
                    print("EEE")
                    if tries == 0:
                        quest -= 1
                        tries = 3
                        print(f"{problem} = {eval(problem)}")
                        break
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                pass
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num = randint(0,9)
    elif level == 2:
        num = randint(10,99)
    else:
        num = randint(100,999)
    return num


if __name__ == "__main__":
    main()
