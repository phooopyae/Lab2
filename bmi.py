def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight))

    bmi = weight /(height*height)

    if bmi < 18.5:  
        print("Under Weight")
        return -1
    elif (18.5 <= bmi <= 25.0):
        print("Normal Weight")
        return 0
    elif bmi>25.0 : 
        print("Over Weight")
        return 1

    print(bmi)


calculate_bmi(weight=57, height=1.73)

