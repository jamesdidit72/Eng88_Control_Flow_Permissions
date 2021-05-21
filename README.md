# Control Flow Age and Permission

## Timings

30 Minutes

## Summary

Simple program to use control flow!

## Tasks

* rules of what the program is supose to do are followed,see bellow

Starter code
```
age = 19
driver_lisence = True


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'

```

## Acceptance Criteria

* is a program that run continuously
* handles strings and integers
* has exist condition
* all business logic works


## First iteration
```python
leave = True
while leave:
    user_prompt = True
    program_end = input('Do you want to continue? Y/N  ')
    print(program_end)
    if program_end.upper() == "Y":
        print('if started')
        while user_prompt:
            age = input('Please enter your age:  ')
            if age.isdigit():
                user_prompt = False
            else:
                print('Please enter a digit')
        driver_license_input = input('Do you have a drivers license? Y/N ')
        if driver_license_input.upper() == 'Y':
            drivers_license = True
        else:
            drivers_license = False
    else:
        print('ended')
        leave = False
```
## Second iteration
```python
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


```