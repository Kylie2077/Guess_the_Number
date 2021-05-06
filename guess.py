import random
random.seed()

while True:
    #'count' variable will count how many tries the player has left to guess
    count = 0
    num = random.randint(1,20)
    guess = int(input("Please guess the number between 1 and 20: "))
    while guess < 1 or guess > 20:
        guess = int(input("Please only guess the number between 1 and 20: "))
    
    if num == guess:
        print("Congratulations! You guessed the right number!")
    else:
        #the program will ask for the number again until all tries run out
        count += 1 
        while count < 5: #the player has 5 tries to guess
            guess = int(input(f"Sorry, please try again. You have {5-count} chances left. "))
            while guess < 1 or guess > 20:
                guess = int(input("Please only guess the number between 1 and 20: "))
            #the program will break if the number is correct.
            if guess == num:
                print("Congratulations! You guessed the right number!")
                break
            count += 1 #'count' will add 1 everytime the player guess wrong
        #if count is equal to 5, that means the user guess wrong in all 5 times.     
        if count == 5:        
            print(f"Sorry. The correct number is {num}.")
        
    #the user will be asked if he/she wish to continue the game
    answer = input("Do you wish to play the game again? (Yes or No) ")
    #the function will only ask to enter yes or no or their abbreviates(y/n)
    #captialized letters can only be entered since all of them will be turned to lower words with lower()
    while (answer.lower().strip() != "no" and answer.lower().strip() != "n" and answer.lower().strip() != "yes" 
    and answer.lower().strip() != "y"):
        answer = input("Please answer yes or no. ")
    #if the answer is 'no' or 'n', the program will stop
    if answer.lower() == "n" or answer.lower() == "no":
        break
    #if the answer is 'yes' or 'y', the while loop will start again 
    elif answer.lower() == "y" or answer.lower() == "yes":
        continue
#the user will receive thank you letter if he/she stops to play
print("Thank you for playing the guessing game!")
