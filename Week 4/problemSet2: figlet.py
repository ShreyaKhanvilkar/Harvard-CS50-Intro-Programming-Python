import sys
from pyfiglet import Figlet
from random import choice

fig = Figlet()

def main():
    if len(sys.argv) == 1:
        font = choice(fig.getFonts())
        fonts("Input: ", font)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fig.getFonts():
        font = sys.argv[2]
        fonts("Input: ", font)
    else:
        sys.exit("Invalid usage")

def fonts(prompt, font):
    user_input = input(prompt)
    fig.setFont(font=font)
    text = fig.renderText(user_input)
    print(f"Output:\n{text}")

main()
