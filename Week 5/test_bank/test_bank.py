from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("heLlO") == 0
    assert value("hello world") == 0


def test_hs():
    assert value("HI") == 20
    assert value("hEy") == 20
    assert value("heya") == 20


def test_others():
    assert value("What's up?") == 100
    assert value("Need something today?") == 100
    assert value("What") == 100


if __name__ == "__main__":
    main()
