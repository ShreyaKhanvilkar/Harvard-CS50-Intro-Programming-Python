def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isnumeric() or s[1].isnumeric():
        return False

    numbers = ""
    letters = ""
    for i in str(s[2:-1]):
        if i.isnumeric():
            numbers += i
        if i.isalpha():
            letters += i
        if i == " " or i == ".":
            return False

    if numbers != "":
        if numbers[0] == "0" or s[-1].isalpha():
            return False

    for i in range(2,len(s)-2):
        if s[i].isnumeric() and s[i+1].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
