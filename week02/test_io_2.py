from unittest import TestCase
from unittest.mock import patch

@patch('sys.argv', ["lab_io_2.py", '+', '1', '1'])
class TestIO_2_1(TestCase):

    def test_io_2_1(self):
        import lab_io_2 as lio2
        assert lio2.result == 2
        
@patch('sys.argv', ["lab_io_2.py", '-', '2', '1'])
class TestIO_2_1(TestCase):
    def test_io_2_1(self):
        import lab_io_2 as lio2
        assert lio2.result == 1