"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Modified by: Fernando Contreras
Assignment: CSD-325 Module 3 - Brownfield + Flowchart
Changes:
  1. Input prompt changed from '> ' to 'fc: ' (initials colon format)
  2. House fee changed from 10% to 12%
  3. Intro updated to include 2 or 7 dice-total bonus notice
  4. Added bonus logic: if dice total equals 2 or 7, player receives +10 mon bonus
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Change 1: Updated intro to include bonus notice for totals of 2 or 7
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

*** BONUS NOTICE: If the dice total is 2 or 7, you receive a 10 mon bonus! ***
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # Change 2: Input prompt changed to initials 'fc: '
        pot = input('fc: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        # Change 3 (also initials prompt): Input prompt changed to initials 'fc: '
        bet = input('fc: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Change 4: Bonus check — if dice total is 2 or 7, award 10 mon bonus
    dice_total = dice1 + dice2
    if dice_total == 2 or dice_total == 7:
        print('Lucky roll! The total was', dice_total, '— you get a 10 mon bonus!')
        purse = purse + 10  # Add the 10 mon bonus to the purse.

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.
        # Change 5: House fee changed from 10% to 12%
        print('The house collects a', pot // 10 + (pot * 2 // 100), 'mon fee.')
        purse = purse - (pot * 12 // 100)  # The house fee is now 12%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()