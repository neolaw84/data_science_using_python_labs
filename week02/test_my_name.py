def test_hello_world(capsys):
    import lab_my_name
    captured = capsys.readouterr()
    assert captured.out
