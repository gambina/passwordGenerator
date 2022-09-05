from pickle import TRUE
import string
import random
import sys

# By default lenght of the password is 16 characters.


def main(lenght=16):
    while lenght < 8:
        print('Password needs to be at least 8 digits')
        try:
            lenght = int(input('Type a number, at least 8:\n'))
        except ValueError as e:
            print('Input needs to be a number')

    # Create basic variables
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    nums = string.digits
    special = string.punctuation
    p_array = []

    # There needs to be at least 1 uppercase, 1 lowercase,
    # 1 number and 1 special character in our password
    p_array.append(lower[random.randint(0, len(lower)-1)])
    p_array.append(upper[random.randint(0, len(upper)-1)])
    p_array.append(nums[random.randint(0, len(nums)-1)])
    p_array.append(special[random.randint(0, len(special)-1)])

    # Creating the rest of the password words/digits
    for i in range(lenght-4):
        key_choice = random.uniform(0, 1)
        if key_choice <= 0.25:
            p_array.append(lower[random.randint(0, len(lower)-1)])
        elif key_choice <= 0.50:
            p_array.append(upper[random.randint(0, len(upper)-1)])
        elif key_choice <= 0.75:
            p_array.append(nums[random.randint(0, len(nums)-1)])
        else:
            p_array.append(special[random.randint(0, len(special)-1)])

    # Now it's time to shuffle the array we created to make sure the sequence will be
    # different
    random.shuffle(p_array)
    password = [''.join(p_array[0:])]
    print(password[0])


if __name__ == '__main__':
    main()
