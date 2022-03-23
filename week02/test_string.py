def test_hello_world(capsys):
    import lab_string
    captured = capsys.readouterr()
    assert "I'm a string," in captured.out
    assert "\n" in captured.out
    assert 'said, "A piece of data"' in captured.out
    with open("lab_string.py") as f:
        program = f.read()
    assert '"""' not in program
    
