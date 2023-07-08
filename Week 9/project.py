from bs4 import BeautifulSoup
import requests
import lxml
import random


def main():
    game()
    print("Thank you for playing. I hope you play again!!!")


def game():
    print("""Welcome to Nationality Quiz!
In this game, you will be given the name of a best-selling fiction author.
You will have to guess their nationality.
You will be given three tries per authors, as well as three lives in total.
Good Luck!\n\n""")
    author_nationality = scrapping()

    lives = 3
    score = 0
    while lives != 0:
        author = generate_author(author_nationality)
        print(f"Author: {author[0]}")
        guess = 3
        while guess > 0:
            user_input = input("Nationality: ").lower()
            if user_input != author[1].lower():
                print("Incorrect.\n")
                guess -= 1
            else:
                print("Congratulations!")
                score += 1
                guess = -1
        print(f"{author[0]} is {author[1]}")
        if guess != -1:
            lives -= 1
        if lives == 1:
            print(f"You have {lives} live left.\n\n")
        else:
            print(f"You have {lives} lives left.\n\n")

    print(f"Game Over. Your score was {score}! Can you get {score+1} points next time?")


def generate_author(a_n):
    return random.choice(list(a_n.items()))


def scrapping():
    html_text = requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_fiction_authors").text
    soup = BeautifulSoup(html_text, "lxml")
    table = soup.find("table")

    authors = []
    for name in table.find_all("span", class_="fn"):
        n = name.a["title"].replace(" (novelist)", "")
        authors.append(n)

    text = table.get_text().strip().split("\n")
    text_list = [i for i in text if i]

    keys = [text_list.index(_)-1 for _ in authors]
    keys.pop(0)
    keys.append(len(text_list)-1)
    keys = iter(keys)

    nationality = {}
    for _ in authors:
        nationality[_] = text_list[next(keys)]

    return nationality


if __name__ == "__main__":
    main()
