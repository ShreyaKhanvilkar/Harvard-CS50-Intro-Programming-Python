import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] != "csv":
        sys.exit("Not a CSV file")

    convert(sys.argv[1], sys.argv[2])


def convert(f1, f2):
    try:
        with open(f1) as file_one:
            reader = csv.DictReader(file_one)
            with open(f2, "w") as file_two:
                writer = csv.DictWriter(file_two, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    writer.writerow({"first" : first, "last" : last, "house" : student["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
