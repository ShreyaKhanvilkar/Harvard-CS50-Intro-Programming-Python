from um import count


def test_dots_and_commas():
    assert count("Hello, um, world") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2


def test_questions():
    assert count("Um... what are regular expressions?") == 1
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2


if __name__ == "__main__":
    main()
