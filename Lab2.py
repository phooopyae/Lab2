import statistics
def display_main_menu(): 
    print("Enter some numbers separated by commas (e.g. 5, 67,32)" )

def get_user_input() : 
    num_in = input()
    numList = num_in.split(",")
    for index in range (len(numList)): 
        numList[index] = int(numList[index])
    return (numList)

def cal_average(numList): 
    total = 0
    for num in numList: 
        total += int(num)
    avg = total/len(numList)
    return(avg)

def find_min_max(numList) : 
    max_num = max(numList)
    min_num = min(numList)
    return [min_num,max_num]

def sort_temperature(numList) :
    numList.sort()
    return (numList)

def calc_median_temperature(List): 
    median = statistics.median(List)
    return median
    

def main(): 
    display_main_menu()
    num_input= get_user_input()
    avg = cal_average(num_input)
    max_min_list =  find_min_max(num_input)
    sorted_list = sort_temperature(num_input)
    median = calc_median_temperature(sorted_list)
    print("This is the average of inputted temperature : " + str(avg))
    print("This is the minimum and maximum temperature : " + str(max_min_list))
    print("This is the list of temperature in ascending order : " , sorted_list)
    print("This is the median of the temperature inputted :", median)


if __name__ == "__main__": 
    main()
