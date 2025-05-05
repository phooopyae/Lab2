def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    #Add code here to calculate BMI
    bmi = weight / (height * height) #bmi = weight / (height**2)
    if (bmi < 18.5):
        print("Under Weight")
        return -1
    elif (bmi >= 18.5 and bmi <= 25.0):
        print("Normal Weight")
        return 0 
    else : 
        print("Over Weight")
        return 1

def main():
   bmi_value = calculate_bmi(1.8,55)
   print(bmi_value)

if __name__ == "__main__":
    main()
