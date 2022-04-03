from unittest import TestCase
from unittest.mock import patch, MagicMock
from functools import partial
from importlib import reload

from cars import Car, Workshop
import lab_control_2 as c2

def good_car_start(self):
    print ("car is started.")
    self.started=True
    self.num_started = self.num_started + 1
    
def bad_car_start(self):
    print ("car won't start.")
    self.started=False
    self.num_started = self.num_started + 1

def not_good_start(self):
    if self.num_started < 1:
        print ("car won't start.")
        self.started = False
    else:
        print ("car starts.")
        self.started = True
    self.num_started = self.num_started + 1
    
auto_good_car = Car(transmission="auto")
auto_good_car.num_started = 0
auto_good_car.start = partial(good_car_start, auto_good_car)
auto_good_car.drive = MagicMock()

auto_bad_car = Car(transmission="auto")
auto_bad_car.num_started = 0
auto_bad_car.start = partial(bad_car_start, auto_bad_car)
auto_bad_car.drive = MagicMock()

auto_not_so_good_car = Car(transmission="auto")
auto_not_so_good_car.num_started = 0
auto_not_so_good_car.start = partial(not_good_start, auto_not_so_good_car)
auto_not_so_good_car.drive = MagicMock()

manual_not_so_good_car = Car(transmission="manual")
manual_not_so_good_car.num_started = 0
manual_not_so_good_car.start = partial(bad_car_start, manual_not_so_good_car)
manual_not_so_good_car.push_start = partial(good_car_start, manual_not_so_good_car)
manual_not_so_good_car.drive = MagicMock()

workshop = Workshop()
workshop.call = MagicMock()

@patch('cars.car', auto_good_car)
class TestControl_2_1(TestCase):

    def test_control_2_1(self):
        reload(c2)
        auto_good_car.drive.assert_called_once()
        assert auto_good_car.num_started == 1

@patch('cars.car', auto_bad_car)
@patch('cars.workshop', workshop)  
class TestControl_2_2(TestCase):
    
    def test_control_2_2(self):
        reload(c2)
        auto_bad_car.drive.assert_not_called()
        workshop.call.assert_called_once()
        auto_bad_car.num_started == 2
        
@patch('cars.car', auto_not_so_good_car)
@patch('cars.workshop', workshop)  
class TestControl_2_3(TestCase):
      
    def test_control_2_3(self):
        reload(c2)
        auto_not_so_good_car.drive.assert_called_once()
        auto_not_so_good_car.num_started == 2
        
@patch('cars.car', manual_not_so_good_car)
@patch('cars.workshop', workshop)  
class TestControl_2_4(TestCase):
      
    def test_control_2_4(self):
        reload(c2)
        manual_not_so_good_car.drive.assert_called_once()
        manual_not_so_good_car.num_started == 3