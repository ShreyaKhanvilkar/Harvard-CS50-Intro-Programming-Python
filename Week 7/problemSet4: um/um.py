import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall("(^|\W)um($|\W)", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
