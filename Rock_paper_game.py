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

game_image = [rock,paper,scissors]

user_choice = int(input("Enter your choice:\n Type 0 for rock,\n Type 1 for paper,\n Type 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
    print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("Computer choose:")
print(game_image[computer_choice])

if user_choice >= 3 and user_choice < 0:
    print("Invalid Option")

elif user_choice ==0 and computer_choice ==2:
    print("You win!")

elif user_choice ==2 and computer_choice ==0:
    print("You loose!")

elif user_choice > computer_choice:
    print("You Win!")

elif computer_choice>user_choice:
    print("you loose!")

elif computer_choice==user_choice:
    print("Its a draw!")
