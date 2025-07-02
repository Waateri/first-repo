import random

secret = random.randint(1, 10)
# Guess the number game
print('I have a number between 1 and 10. Can you guess it?')
guess = None
tries = 0
max_tries = 5

while guess != secret and tries < max_tries:
   try:
    guess = int(input(f'Guess the number (1-10). Tries left: {max_tries - tries}:  '))
    tries += 1
    if guess < secret:
        print('Too low!')
    elif guess > secret:
        print('Too high!')
   except ValueError:
    print('Please enter a valid number.')
  
if guess == secret:
    print('You got it!')
else:
   print(f'You ran out of tries. The number was {secret}. Better luck next time!')
