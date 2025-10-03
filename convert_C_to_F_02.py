# FILE NAME - convert_C_to_F_02.py

# NAME: ANTONIO SANTIAGO  
# DATE: 10/1/2025 
# BRIEF DESCRIPTION: Program that asks user if they would like to convert Celsius to Fahrenheit or Fahrenheit to Celsius. Then process thier temperature.   



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    convertTemp()

def convertTemp():
    
    print('===== Temperature Converter =====')
    print('\n 1. Convert from Celsius to Fahrenheit \n 2. Convert from Fahrenheit to Celsius\n')
    
    option = int(input("Please choose from the above menu: "))
    temperature = float(input("Enter a temperature to convert: "))
    
    if option == 1:
        tempConverted = temperature * 9/5 + 32
        print(f"{temperature} degrees Celsius is {tempConverted} degrees Fahrenheit.")

    elif option == 2:
        tempConverted = (temperature - 32) * 5/9
        print(f"{temperature} degrees Fahrenheit is {tempConverted} degrees Celsius.")



main()







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
I can choose between an elif statement or a else statement depending on how many outcomes I want to control. 






'''




'''
