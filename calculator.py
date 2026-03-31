import subprocess

first_number = int(input("Number: "))
while True:
    
    sec_num = int(input("Number: "))

    print(""" Select the action to be performed. 
      
            1.Addition
            2.Subtraction 
            3.Multiplication 
            4.Division  
      """)

    numerical_operations = int(input("Select the action to be performed: "))

    match numerical_operations:
        case 1:
            first_number = first_number + sec_num
            print(first_number)
            print('')
        case 2:
            first_number = first_number - sec_num
            print(first_number)
            print('')
        case 3:
            first_number = first_number * sec_num
            print(first_number)
            print('')
        case 4:
            first_number = first_number / sec_num
            print(first_number)
            print('')
    
