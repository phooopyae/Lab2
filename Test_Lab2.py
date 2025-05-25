import Lab2.Lab2 as lab2

def test_find_minmax(): 
    input_list = [5,1,8,99,32]
    test_result = [1,99]
    result = lab2.find_min_max(input_list)
    assert (result == test_result)

def test_cal_average(): 
    input_list = [5,1,8,99,32]
    result = lab2.cal_average(input_list)
    assert (result == 29)

def test_cal_median_temperature():
    input_list = [5,1,8,99,32]
    result = lab2.calc_median_temperature(input_list)
    assert(result == 8)