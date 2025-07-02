# Ask from User their name, and to keep a number in their mind
user_name_1 = input("Welcome User 1. Enter your name: ")
user_input_1 =  input(f"Hi {user_name_1}, Let's play 'Guess Number' game.\n Memorize a number: ")
if user_input_1.replace('.', '', 1).isdigit():
    if "." in user_input_1:
        secret_number= float(user_input_1)
        #print("The number is a float")
    else:
        secret_number= int(user_input_1)
        #print("The number is an integer")

    # ask another User their name, and to guess numbers till they guess the secret number
    user_name_2 = input("Welcome User 2. Enter your name: ")
    user_input_2 = input(f"Hi {user_name_2}, Let's play 'Guess Number' game.\n Guess the Secret Number: ")
    if user_input_2.replace('.', '', 1).isdigit():
        if "." in user_input_2:
            guess_number = float(user_input_2)
            guess_number = abs(guess_number)
            # print("The number is a float")
        else:
            guess_number = int(user_input_2)
            guess_number = abs(guess_number)
            # print("The number is an integer")

        guess_count = 0
        while True:
            guess_count += 1
            if guess_number > secret_number:
                print("Too high :( ")
            if guess_number < secret_number:
                print("Too low :( ")
            if guess_number == secret_number:
                if guess_count == 1:
                    print("Congrats {}! You guessed the Secret Number in {} attempt.".format(user_name_2, guess_count))
                else:
                    print("Congrats {}! You guessed the Secret Number in {} attempts.".format(user_name_2, guess_count))
                break
            guess_number = input("Guess another number: ")
            if guess_number.replace('.', '', 1).isdigit():
                if "." in guess_number:
                    number = float(guess_number)
                    #print("The number is a float")
                else:
                    number = int(guess_number)
                    #print("The number is an integer")
                guess_number = number
            else:
                print("Please enter a number.")
                break
    else:
        print("Please enter a digit.")
else:
    print("Please enter a digit.")

