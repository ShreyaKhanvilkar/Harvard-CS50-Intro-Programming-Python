import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-2:] != "py":
        sys.exit("Not a Python file")

    print(lines(sys.argv[1]))


def lines(f):
    try:
        count = 0
        with open(f) as file:
            for line in file:
                if line.strip() != "":
                    if line.lstrip()[0] != "#":
                        count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
