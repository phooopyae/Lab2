def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    #Add code here to calculate BMI
    bmi = weight / (height * height) #bmi = weight / (height**2)
    return bmi
'''
    #Add code here to display calculate BMI
    print("This is calculated BMI" + str(bmi))

    #determine if the useris under weight or normal weight or over weight
    if bmi < 18.5 :
        print("Under Weight")
    elif (bmi >= 18.5) and (bmi <= 25.0) :
        print("Normal Weight")
    elif bmi >25.0 : 
        print("Over Weight")
'''
def classify_bmi(bmi_value):
    if (bmi_value < 18.5):
        print("Under Weight")
    elif (bmi_value >= 18.5 and bmi_value <= 25.0):
        print("Normal Weight")
    else : 
        print("Over Weight")
    return

def main():
    bmi_output = calculate_bmi(1.8, 55) 
    print("bmi_value : " + str(bmi_output))
    classify_bmi(bmi_output)

if __name__ == "__main__":
    main()
