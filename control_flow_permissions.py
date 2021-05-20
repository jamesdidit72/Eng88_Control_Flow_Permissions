leave = True
while leave:
    user_prompt = True
    continue_ = input('Do you want to continue? Y/N  ')
    if continue_.upper == 'Y':
        while user_prompt:
            age = input('Please enter your age:  ')
            if age.isdigit():
                user_prompt = False
            else:
                print('Please enter a digit')
        driver_license_input = input('Do you have a drivers license? Y/N ')
        if driver_license_input.upper == 'Y':
            drivers_license = True
        else:
            drivers_license = False
    else:
        leave = False