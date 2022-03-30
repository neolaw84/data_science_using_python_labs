import io
from unittest import TestCase

def test_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('42'))
    import lab_io_1
    assert lab_io_1.a == "42"
    assert lab_io_1.i == 42