import random

a_1 = random.randint(1, 6)
b_1 = random.randint(1, 6)

user_1 = a_1 + b_1
 
a_2 = random.randint(1, 6)
b_2 = random.randint(1, 6)

user_2 = a_2 + b_2

if user_1 > user_2:
    print("winner player 1")
elif user_1 < user_2:
    print("winner player 2")
else:
    print("There is a tie between you") 