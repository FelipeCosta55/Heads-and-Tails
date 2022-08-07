import random

user_choice = input("Do you choose Heads or Tails?:\n")
if user_choice == "Heads":
  user_choice = 0   #Heads = 0
  print("You choose Heads.")
else:
  user_choice = 1   #Tails = 1
  print("You choose Tails.")

random_toss = random.randint(0, 1)
if random_toss == 0:
  print("The toss resul was Heads.")
  if user_choice == 0:
    print("You win!")
  elif user_choice == 1:
    print("You loose!")
elif random_toss == 1:
  print("The toss result was Tails.")
  if user_choice == 0:
    print("You loose!")
  elif user_choice == 1:
    print("You win!")