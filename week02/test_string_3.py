import pathlib

THIS_FILE_PATH = pathlib.Path(__file__)
THIS_DIR_PATH = THIS_FILE_PATH.parent

def test_string_3(capsys):
    import lab_string_3 as ls
    captured = capsys.readouterr()
    output = captured.out
    with open(str(THIS_DIR_PATH.joinpath("lab_string_3.py")), "rt") as f:
        program = f.read()
    assert output.strip().replace("  ", " ").lower() == "the ultimate answer is 42"
    assert "format(" not in program