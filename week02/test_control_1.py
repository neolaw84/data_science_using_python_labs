from unittest import TestCase
from lab_control_1 import add_or_subtract as aos
from lab_control_1 import arithmetic as ari

class TestControl1(TestCase):
    def test_add(self): 
        assert aos('+', 5, 2) == 7
        assert ari('+', 9, 7) == 16
        
    def test_sub(self):
        assert aos('-', 5, 2) == 3
        assert ari('-', 9, 7) == 2
        
    def test_div(self):
        assert ari('/', 5, 2) == 2.5
        with self.assertRaises(NotImplementedError):
            ari('/', 5, 0)