from random import randint

while True:
    try:
        n = int(input("Level: "))
        x = randint(1, n)
        while True:
            guess = int(input("Guess: "))
            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            else:
                print("Just right!")
                raise EOFError
    except EOFError:
        break
    except ValueError:
        pass
