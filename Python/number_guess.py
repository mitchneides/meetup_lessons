upper_limit = 1000
lower_limit = 1
current_guess = 500
attempts = 1

print("Welcome to the guessing game!")
print("Think of a number between 1 and 1000... Don't forget it!\n")
while True:
    print("\nIs your number " + str(current_guess) + "?")
    feedback = input("Enter 0 if your number is lower, 2 if your number is higher, or 1 if I was correct: ")
    
    if feedback == "0":
        upper_limit = current_guess
        current_guess = (upper_limit - lower_limit)//2 + lower_limit
        attempts += 1
    elif feedback == "2":
        lower_limit = current_guess
        current_guess = ((upper_limit - lower_limit)//2) + lower_limit
        attempts += 1
    elif feedback == "1":
        print("\nCool! I guessed your number in " + str(attempts) + " attempts!")
        break
    else:
        print("You must input 0, 1 or 2. Try again...")
