def test_rec():
    from lab_variable_3 import area_of_rectangle
    
    assert area_of_rectangle(3, 5.0) == 3 * 5.0
    assert area_of_rectangle(5, breadth=8.99) == 5 * 8.99
    assert area_of_rectangle(1, 1) == 1
    
def test_tri():
    from lab_variable_3 import area_of_triangle
        
    assert area_of_triangle(3, 5.0) == 3 * 5.0 * 0.5
    assert area_of_triangle(5, height=8.99) == 5 * 8.99 * 0.5
    assert area_of_triangle(1, 1) == 0.5
    
def test_cir():
    from lab_variable_3 import area_of_circle
    
    from math import pi
    assert area_of_circle(3) == 3 * 3 * pi
    assert area_of_circle(5) == 5 * 5 * pi
    assert area_of_circle(1) == pi