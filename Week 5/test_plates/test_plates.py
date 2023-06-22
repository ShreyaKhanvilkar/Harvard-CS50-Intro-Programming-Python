from plates import is_valid


def test_startletters():
    assert is_valid("ABCDE") == True
    assert is_valid("A2CDEF") == False
    assert is_valid("1ABCDE") == False


def test_characters():
    assert is_valid("o") == False
    assert is_valid("12") == False
    assert is_valid("12ABCDE") == False


def test_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA02A") == False


def test_marks():
    assert is_valid("12 ABC") == False
    assert is_valid("12.ABC") == False
    assert is_valid("!12ABC") == False

def test_others():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False



if __name__ == "__main__":
    main()
