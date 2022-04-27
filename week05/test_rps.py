import io
from unittest.mock import patch
from unittest import TestCase

import pytest

import sys
if "." not in sys.path:
    sys.path.append(".")

from lab_rps import ask_exit, main

@patch('builtins.input', side_effect=['Y'])
class TestAskExitY(TestCase):
    def test_ask_exit(self, capsys):
        assert ask_exit()
        
@patch('builtins.input', side_effect=['N'])
class TestAskExitN(TestCase):
    def test_ask_exit(self, capsys):
        assert not ask_exit()
        
@patch('builtins.input', side_effect=['B', '1', 'Y'])
class TestAskExitNNY(TestCase):
    def test_ask_exit(self, capsys):
        assert ask_exit()
        
ROCK=0
PAPER=1
SCISSOR=2        

@patch("builtins.input", side_effect=["R", "N", "S", "Y"])
@patch("random.randint", side_effect=[ROCK, PAPER])
class TestMain11(TestCase):
    
    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
        
    def test_main_11(self, mock_randint, mock_input):
        main()
        out, _ = self.capfd.readouterr()
        tokens = [nab.lower() for nab in out.split() if nab.lower() in ["neither", "player_a", "player_b"]]
        self.assertListEqual(tokens, ["neither", "player_a"])

@patch("builtins.input", side_effect=["R", "Y"])
@patch("random.randint", side_effect=[ROCK])
class TestMain12(TestCase):
    
    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
        
    def test_main_12(self, mock_randint, mock_input):
        main()
        out, _ = self.capfd.readouterr()
        tokens = [nab.lower() for nab in out.split() if nab.lower() in ["neither", "player_a", "player_b"]]
        self.assertListEqual(tokens, ["neither"])

@patch("builtins.input", side_effect=["R", "N", "R", "N", "R", "Y"])
@patch("random.randint", side_effect=[ROCK, PAPER, SCISSOR])
class TestMain13(TestCase):
    
    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
        
    def test_main_13(self, mock_randint, mock_input):
        main()
        out, _ = self.capfd.readouterr()
        tokens = [nab.lower() for nab in out.split() if nab.lower() in ["neither", "player_a", "player_b"]]
        self.assertListEqual(tokens, ["neither", "player_b", "player_a"])

