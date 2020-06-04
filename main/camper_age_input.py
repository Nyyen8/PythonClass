"""
Program: camper_age_input.py
Author: Paul Elsea
Last Modified: 06/04/2020

The purpose of this program is to accept an infant's age,
convert the age into months, then prints the result.
"""
def valid_int_check():
    global user_input_age
    '''This gives the function access to the variable used to generate the final result'''
    print("Student's age in years from 1 to 5: ")
    while True:
        '''This while loop continues until a valid input is entered'''
        try:
            user_input_age = int(input())
            if user_input_age >= 1:
                if user_input_age <= 5:
                    break
                    '''This causes the loop to end'''
                else:
                    print("Please enter an age from 1 to 5")
            else:
                print("Please enter an age from 1 to 5 years")

        except ValueError:
            print("Please enter an age using digits('1', '2', etc).")
            continue
            '''This is triggered if a non-integer is entered, resetting the loop'''
'''This function checks to make sure user input an integer from 1 to 5'''

def convert_to_months(age):
    '''This takes the user's input and multiplies it by 12 and returns the result'''

    age_in_months = age * 12
    return age_in_months

if __name__ == '__main__':
    '''This defines a default variable, calls the valid_input_check method, then the convert_to_months method,
    then prints the result.'''
    user_input_age = 0
    valid_int_check()
    age_result = convert_to_months(user_input_age)
    print(age_result)