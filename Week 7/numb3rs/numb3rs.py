import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    address = "((?:[2][0-5]|[1]\d|\d)?\d)"
    if match:= re.search(r"^" + address + "\." + address + "\." + address + "\." + address + "$", ip):
        for i in range(5):
            if len(match.group(i)) == 3 and match.group(i)[0] == "2" and match.group(i)[1] == "5" and match.group(i)[2] > "5":
                return False
        return True
    return False


if __name__ == "__main__":
    main()
