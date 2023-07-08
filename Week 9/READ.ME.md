  # Best Selling Fiction Authors: Nationality Guessing Game

    #### Video Demo: <https://youtu.be/06RueyXckhY>


    #### Description:

    ----------------------------------------REQUIREMENTS.TXT----------------------------------------

    I have used two pip-installable library for this project.
    There were beautifulsoup4 and lxml libraries.
    I used beautifulsoup4 to web scrap a list of best selling fiction authors from Wikipedia.
    I used lxml as a binding library in order to make the webscrapping using beautifulsoup4 work.

    ----------------------------------------TEST_PROJECT.PY---------------------------------------

    test_game():
    tests the game() function

    test_generate_author():
    tests the generate_author() function

    test_scrapping():
    tests the test_scrapping() function

    ----------------------------------------WEB_SCRAPPER.PY----------------------------------------

    main():
    runs game() in order to bring the program to life
    after the user completes the game, a message of gratitude is printed to the user

    game():
    prints a welcome message to the user and explains the rules of the game
    uses scrapping() to all information pertaining to the author that is needed
    lives and score are set to 0
    while the user has not used up all of their lives
    a random author's name is chosen [by generate_author(a_n)] for the user to guess their nationality
    if the user correctly guesses the author's nationality within three guesses,
    they earn a point and are prompted with another author's name
    otherwise they lose a life and are shown the author's correct nationality
    the user is prompted with the score when they run out of lives

    generate_author(a_n):
    random.choice is used to select an author from the curated list of authors
    this author and their nationality is then returned as a tuple for game() to unpack

    scrapping():
    using requests, beautifulsoup4, and lxml, the best-selling fiction authors table is found
    all of the authors names are extracted using class "fn" where .replace(" (novelist)", "") is used to clean up the data
    these author names added to a list of authors using a for loop
    full text from the table is extracted, whitespaces are stripped, and the text is split on new lines
    all empty strings are removed using list comprehension
    the index of all the author's names are found and taking the index before it,
    the index of the previous author's nationality is found and add to a list using list comprehension
    the first element of this list is popped as it is not list the list
    the last value in the text is added to the list as it is the nationality of the last author
    this list is turned into a iterable list for easy access to subsequent values in the list
    a dictionary is made with the key being the author's name and their respective nationality and returned
