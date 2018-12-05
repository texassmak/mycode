#!/usr/bin/env python3
round = 0           # integer round initiated to 0
while(True):        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input()    # string answer collected from user
    if(answer == 'Brian' or answer == 'brian'): # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif(round == 3):    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')
    if(answer == 'shrubbery'): # logic for the secret answer
        print('You gave the super secret answer!')
        break


	