from summ import calculate as cal

def test(a,b):
    c = cal(a,b)

    test_c = a+b

    assert c == test_c


test(5,15)
test(10,50)
test(13,311)
