import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] != "csv":
        sys.exit("Not a CSV file")

    print(format_table(sys.argv[1]))


def format_table(f):
    try:
        with open(f) as file:
            reader = csv.reader(file)
            return tabulate(reader, headers = "firstrow", tablefmt = "grid")
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
