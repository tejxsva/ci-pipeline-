from hello import greet

def test_greet():
    assert greet("Tejas") == "Hello Tejas"

def test_greet_another():
    assert greet("World") == "Hello World"
