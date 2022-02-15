def test_hello_world(capsys):
    import lab_hello_world_burmese
    captured = capsys.readouterr()
    assert "မင်္ဂလာပါ" in captured.out
    assert "ကမ္ဘာကြီး" in captured.out

