import random

print("Welcome to High or Low, when presented a number guess if the next number will he higher or lower. Try to reach 10 points to win!\n")

num = 5
score = 0
# def new_num():
#     random.randint(1,10)

while score < 11:
    print("The current number is ", num, "\n Will the next number be higher or lower?")
    player_guess = input()
    rand_num = random.randint(1, 10)
    if player_guess == "higher" and rand_num > num:
        print("Correct! You gain a point!")
        num = rand_num
        score += 1
    elif player_guess == "lower" and rand_num < num:
        print("Correct! You gain a point!")
        num = rand_num
        score += 1
    elif num == rand_num:
        print("It was the same! Try again")
    elif player_guess == "higher" and rand_num < num:
        print("Wrong! Better luck next time.")
        print("Your final score was", score)
        break;
    elif player_guess == "lower" and rand_num > num:
        print("Wrong! Better luck next time.")
        print("Your final score was", score)
        break;
    else: 
        print("Please enter 'higher' or 'lower'")

