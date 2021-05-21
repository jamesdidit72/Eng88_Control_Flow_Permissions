parameter_list = [
    'You can vote and drive',
    'You can vote',
    'You can drive',
    'you cant legally drink but your mates/uncles might have your back',
    'Youre too young, go back to school!'
]
display_list = []

leave = True
while leave:
    program_end = input('Do you want to continue? Y/N  ')
    display_list = []
    if program_end.upper() == "Y":
        age = int(input('Please enter your age:  '))
        driver_license_input = input('Do you have a drivers license? Y/N ')
        if driver_license_input.upper() == 'Y':
            drivers_license = True
        else:
            drivers_license = False
        if age <= 12:
            display_list.append(parameter_list[4])
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
        for parameter in display_list:
            print(parameter)
    else:
        leave = False

