from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    print(minutes(input("Date of Birth: ")))


def minutes(d):
    try:
        days = (date.today() - date.fromisoformat(d)).days
        minutes = days * 24 * 60
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
