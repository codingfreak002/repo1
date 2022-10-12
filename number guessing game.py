import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
a = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
cnt = 0
while cnt < math.log(upper - lower + 1, 2):
    cnt += 1
    guess = int(input("Guess a number:- "))
    if a == guess:
        print("Congratulations you did it in ",
              cnt, " try")
        break
    elif a > guess:
        print("You guessed too small!")
    elif a < guess:
        print("You Guessed too high!")
if cnt >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % a)
    print("\tBetter Luck Next time!")
