import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[2][-4:] not in [".jpg", "jpeg", ".png"]:
        sys.exit("Invalid output")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

    overlay(sys.argv[1], sys.argv[2])


def overlay(before, after):
    try:
        shirt = Image.open("shirt.png")
        muppet = Image.open(before)
        crop = ImageOps.fit(muppet, shirt.size)
        crop.paste(shirt, mask=shirt)
        crop.save(after)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
