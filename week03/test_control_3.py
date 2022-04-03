from lab_control_3 import total_mark

def test_control_3():
    assert total_mark(answer_1 = True, answer_2 = 'B', answer_3 = 42, answer_4 = False) == 100
    assert total_mark(answer_1 = True, answer_2 = 'C', answer_3 = 42, answer_4 = False) == 75
    assert total_mark(answer_1 = True, answer_2 = 'B', answer_3 = 41, answer_4 = False) == 65
    assert total_mark(answer_1 = False, answer_2 = 'B', answer_3 = 42, answer_4 = True) == 60