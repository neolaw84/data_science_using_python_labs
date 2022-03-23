def test_hello_world(capsys):
    import lab_my_name
    captured = capsys.readouterr()
    assert "my name is" in captured.out.strip().lower()
