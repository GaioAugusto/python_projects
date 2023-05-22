import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


choices = [rock, paper, scissors]

h_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if h_choice in [0, 1, 2]:
    print(choices[h_choice])
    print("Computer chose:")
    c_choice = random.randint(0, 2)
    print(choices[c_choice])

    if h_choice == c_choice:
        print("It's a tie.")
    elif (h_choice == 0 and c_choice == 2) or (h_choice == 1 and c_choice == 0) or (h_choice == 2 and c_choice == 1):
        print("You win.")
    else:
        print("You lose.")

else:
    print("Invalid move. Game Over.")


