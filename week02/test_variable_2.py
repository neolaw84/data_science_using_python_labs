def test_var_1():
    import lab_variable_2 as m
    assert m.price == 99.99
    assert m.quantity == 5
    assert m.VAT == 0.10
    tot = m.price * m.quantity
    assert m.total == tot + tot * m.VAT