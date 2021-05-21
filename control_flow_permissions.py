parameter_list = [
    'You can vote and drive',
    'You can vote',
    'You can drive',
    'you cant legally drink but your mates/uncles might have your back',
    'Youre too young, go back to school!'
]  # list containing the available outputs
display_list = []  # empty list to display the outcomes

leave = True
while leave:  # loop continues until leave = False

    age = int(input('Please enter your age:  '))  # asks for the age
    driver_license_input = input('Do you have a drivers license? Y/N ')  # asks if they have a drivers license
    if driver_license_input.upper() == 'Y':  # checks the input
        drivers_license = True
    else:
        drivers_license = False
    if age <= 12:
        display_list.append(parameter_list[4])  # adds index 4 from parameter_list to display_list
    elif age > 17 and drivers_license:
        display_list.append(parameter_list[0])
    elif age > 17:
        display_list.append(parameter_list[1])
    elif drivers_license:
        display_list.append(parameter_list[2])
    elif age < 18:
        display_list.append(parameter_list[3])
    else:
        print('didnt work')
    for parameter in display_list:  # displays the display_list in a clean manner
        print(parameter)
    program_end = input('Press any key to continue, or type "exit" to leave: ')
    display_list = []  # clears list for next user
    if program_end.upper() == "EXIT":  # checks if the input == "exit"
        leave = False  # ends loop
        print("Exiting...")
    else:
        continue  # starts loop from the beginning


