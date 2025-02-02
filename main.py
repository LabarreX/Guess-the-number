from random import *

def main(games, wins) :
  games += 1
  print("Guess a number between 1 and 1000\n")
  answer = randint(1,1000)
  attempts = 0
  while attempts < 10 :
    guess = input("Enter your guess : ")
    if guess == "cheat" :
      print("Answer is ", answer)
    else :
      try :
        guess = int(guess)
      except :
        print("Please enter a number")
        while type(guess) != int :
          guess = input("Enter your guess, which MUST be an integer : ")
          try :
            guess = int(guess)
          except :
            continue
      if guess < answer:
        print("Your number is too low")
      elif guess > answer:
        print("Your number is too high")
      else :
        print(f"\nYou won in {attempts+1} attempts !")
        wins +=1
        break
    attempts += 1
    print(f"\nOnly {10-attempts} attempts left !")

  if attempts == 10:
    print(f"\nYou lost !\nThe answer was {answer}")

  if input(f"\nPlay again ? (y/n) ") == "y":
    print("\n\n------------------------------------------------\n\n")
    main(games, wins)
  else :
    print(f"\nYou won {wins} of {games} games, or a {round(wins*100/games, 1)}% success rate !")


main(0,0)
