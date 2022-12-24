#!/usr/bin/python3
import random

print(f'Enter value less than 10')

#this function processes the score
def score_keeper(int):
    sum = int + 1
    return sum

#score1 is a variable that get updated from 'score1' variable from checker
score1 =score_keeper(0)

def checker(string):
    #To handle character change to int
    comparator = int(correct)
    
    if comparator != 0:
        if comparator%2 == 0:
            print(f"Hint: an even number!")
        else:
            print(f"Hint: an odd number!")
    else:
        print(f"Hint: people  don't usually rate me")
    user_input1 = input('Enter your guess: ')

    #comparing generated value with user input
    if correct == user_input1:
        score1 = 1
        print(f"Yes, you're correct, the answer is {correct}. You earn {score1}")
    else:
        print(f"nice effort, the answer is {correct} , better luck next time")
    
#Loop to through to change value
for i in range(1,6):
    first_number = chr(random.randint(48, 57))
    correct =first_number
    first_number = checker(first_number)
    total = score1
    #total collect scores while looping is going on
total = score_keeper(total)
print(f'Your have 3 Bonus point,  total point is {total + 3} !')


