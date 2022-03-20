import os

def test_environment():
    my_var = os.environ["MY_VAR"]
    assert "hello" == my_var
    assert "week01" in os.getcwd()