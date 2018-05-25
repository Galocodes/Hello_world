"""This program rolls a pair of dice and asks the user to guess a number. If the user's guess is greater than or equal to the total value of the roll, they win! Otherwise, the computer wins."""
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input('Guess a number: '))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print 'Max possible roll is %d' % max_val
  guess = get_user_guess()
  if guess > max_val:
    print 'Invalid guess.'
  else:
    print 'Rolling...'
    sleep(2)
    print 'First roll is %d.' % first_roll
    print 'Second roll is %d.' % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print 'Total roll is %d.' % total_roll
    print 'Result...'
    sleep(1)
    if guess > total_roll:
      print 'You Win!'
    else:
      print 'You Lose.'

roll_dice(6)
