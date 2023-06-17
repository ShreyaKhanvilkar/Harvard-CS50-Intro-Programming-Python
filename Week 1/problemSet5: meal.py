def main():
    user_input = convert(input("What time is it?: "))
    if user_input >= 7.0 and user_input <= 8.0:
        print("breakfast time")
    elif user_input >= 12.0 and user_input <= 13.0:
        print("lunch time")
    elif user_input >= 18.0 and user_input <= 19.0:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    m = float(m) / 60
    return float(h) + m


if __name__ == "__main__":
    main()
