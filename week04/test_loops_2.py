from lab_loops_2 import get_total_mark

# [10, 45, 20, 35, True, 90, 33, False, 80, 11] တပုဒ် ၁၀ မှတ်၊ boolean True/False မှားလျှင် အမှတ် ၆၀ ကျော်ပါက ၆၀ သို့ ပြန်ချပါ။
# [10, 4, 20, True, True, 90, 33, True, 8, 0] တပုဒ် ၁၀ မှတ်၊ boolean True/False မှားလျှင် အမှတ် ၆၀ ကျော်ပါက ၆၀ သို့ ပြန်ချပါ။

def test_1_1():
    correct = [10, 45, 20, 35, True, 90, 33, False, 80, 11]
    student = [10, 45, 20, 35, True, 80, 33, False, 80, 10]
    assert get_total_mark(correct, student) == 80
    
def test_1_2():
    correct = [10, 45, 20, 35, True, 90, 33, False, 80, 11]
    student = [10, 45, 20, 35, True, 80, 33, True, 80, 10]
    assert get_total_mark(correct, student) == 60