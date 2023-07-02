from seasons import minutes


def test_ninties():
    assert minutes("1999-12-12") == "Twelve million, three hundred eighty-eight thousand, three hundred twenty minutes"
    assert minutes("1996-10-04") == "Fourteen million, sixty-four thousand, four hundred eighty minutes"


def test_twenties():
    assert minutes("2020-02-02") == "One million, seven hundred ninety-four thousand, two hundred forty minutes"


def test_my_birthday():
    assert minutes("2006-10-04") == "Eight million, eight hundred five thousand, six hundred minutes"


if __name__ == "__main__":
    main()
