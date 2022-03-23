def test_var_1():
    import lab_variable_1 as m
    assert m.a == 10
    assert m.b == 10.0
    assert type(m.a) is int 
    assert m.c is False