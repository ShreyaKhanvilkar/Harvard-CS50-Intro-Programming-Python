from twttr import shorten


def test_twttr():
    assert shorten("qaqeqiqoquq") == "qqqqqq"

def test_twttr_capital():
    assert shorten("QAqeqiqoqUQ") == "QqqqqQ"

def test_twttr_numbers():
    assert shorten("9aqeqiqoqu9") == "9qqqq9"

def test_twttr_punct():
    assert shorten("!aqeqiqoqu!") == "!qqqq!"


if __name__ == "__main__":
    main()
