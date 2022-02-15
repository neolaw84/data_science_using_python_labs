def test_hello_world(capsys):
    import lab_hello_world
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

