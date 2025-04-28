def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    #Add code here to calculate BMI
    bmi = weight / (height * height)

    #Add code here to display calculate BMI
    print("This is calculated BMI" + str(bmi))

    #determine if the useris under weight or normal weight or over weight
    if bmi < 18.5 :
        print("Under Weight")
    elif (bmi >= 18.5) and (bmi <= 25.0) :
        print("Normal Weight")
    elif bmi >25.0 : 
        print("Over Weight")


calculate_bmi(weight=57, height=1.73) 