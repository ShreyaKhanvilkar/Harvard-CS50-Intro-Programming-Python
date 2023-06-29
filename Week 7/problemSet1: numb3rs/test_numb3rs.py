from numb3rs import validate


def test_true():
    assert validate("255.255.255.255") == True


def test_false():
    assert validate("512.512.512.512") == False


def test_first_byte():
    assert validate("59.981.99.19") == False


if __name__ == "__main__":
    main()
