#print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") 
def display_main_menu():
    print("Enter some numbers separated by comma (eg. 5, 67, 32) ")

def get_user_input():
    temps = input()
    temps = temps.split(",")
    temps = [float(index) for index in temps]
    return temps

def calc_average_temperature(temp_list):
    total_temp = 0
    for index in temp_list:
        total_temp = total_temp + index
    avg_temp = total_temp / len(temp_list)
    return avg_temp

def calc_min_max_temperature(temp_list):
    min_max_temp = [min(temp_list), max(temp_list)]
    return min_max_temp


def calc_median_temperature(temp_list):
    temp_list = sorted(temp_list)
    
    if ((len(temp_list))% 2 == 0): 
        index = len(temp_list) // 2
        median = (temp_list[index] + temp_list[index-1]) / 2
    else : 
        index = len(temp_list) //2 
        median = temp_list[index]
    return median

display_main_menu()
temps = get_user_input()
print("This is average " + str(calc_average_temperature(temps)))
print("This is [min,max] " + str(calc_min_max_temperature(temps)))
print(calc_median_temperature(temps))