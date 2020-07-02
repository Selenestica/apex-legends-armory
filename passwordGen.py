
import random
import string

random_list1 = ['Space', 'Radiate', 'Nine', 'Answer', 'Educate', 'Entertaining', 'Range', 'Teeny', 'Watery', 'Impress',
                'Tease', 'Subtract', 'Position', 'Loyalty', 'Sticky', 'Dividend', 'Advocate', 'Enter', 'Hill',
                'Craftsman', 'Hike', 'Farewell']

random_list2 = ['Halt', 'Flourish', 'Officer', 'Hospitality', 'Operation', 'Cart', 'Relative', 'Insist', 'Epic',
                'Wind', 'Cheat', 'Dividend', 'Cooperate', 'Get', 'Bell', 'Horror', 'Rotation', 'Cap', 'Grip', 'Roof']

print("Welcome to the Password Generator! I've created three randomly generated, strong passwords for you below :)")
generating = True

while generating:

    for num in range(3):

        capital_word = random.choice(random_list1)
        random_word = random.choice(random_list2)

        number = random.randrange(100, 999)

        special_char = random.choice(string.punctuation)
        special_char2 = random.choice(string.punctuation)

        password = capital_word + str(number) + special_char + random_word
        print("\n" + password)

    not_yes_or_no = True
    while not_yes_or_no:
        response = input("\nWant different passwords?\n")
        response = response.lower()
        if response == "no":
            not_yes_or_no = False
            generating = False
        elif response == "yes":
            not_yes_or_no = False
            generating = True
        else:
            print("\nPlease just type 'Yes' or 'No'...\n")


print("\nOkay! Make sure you don't forget your new password!")
