from lab_loops_1 import add_numbers_between
def test_loops_1_1():
    data = [1, 2, 3, 4, 5]
    assert add_numbers_between(data) == 0
    
def test_loops_1_2():
    data = [1, 2, "start", 3, 4]
    assert add_numbers_between(data) == 7
    
def test_loops_1_3():
    data = [1, 2, "start", 3, 4, 5, "stop", 9, 10]
    assert add_numbers_between(data) == 12
    
def test_loops_1_4():
    data = ["start", 1, "stop"]
    assert add_numbers_between(data) == 1
    
def test_loops_1_5():
    data = [1, 2, "start"]
    assert add_numbers_between(data) == 0