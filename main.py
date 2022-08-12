import random

print("Choose: Rock, Paper or Scissor")
player = input("You: ")
list = ["Rock", "Paper", 'Scissor']
Bot = random.choice(list)
if player == "Rock":
    if Bot == 'Rock':
        print("Bot:", Bot)
        print("Its a tie")
    if Bot == 'Paper':
        print("Bot:", Bot)
        print("You lost")
    if Bot == 'Scissor':
        print("Bot:", Bot)
        print("You won")
if player == "Paper":
    if Bot == 'Rock':
        print("Bot:", Bot)
        print("You won")
    if Bot == 'Paper':
        print("Bot:", Bot)
        print("Its a tie")
    if Bot == 'Scissor':
        print("Bot:", Bot)
        print("You lost")
if player == "Scissor":
    if Bot == 'Rock':
        print("Bot:", Bot)
        print("You lost")
    if Bot == 'Paper':
        print("Bot:", Bot)
        print("You won")
    if Bot == 'Scissor':
        print("Bot:", Bot)
        print("Its a tie")
if player != 'Paper' and player != 'Rock' and player != "Scissor":
    print('Error! Choose Rock, Paper or Scissor')