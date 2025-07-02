import random
import sys

print('Welcome to space roamers! Do you wish to step into teleport (yes/no)?')

teleport_choice = input(str('Make decision: '))

if teleport_choice == 'yes':
    print('Journey begins!')
elif teleport_choice == 'no':
    print('You are a disappointment')
    sys.exit()
else:
    print('Invlaid choice. Exiting game.')
    sys.exit()

teleport = random.randint(0, 2)


if teleport == 0:
    print('You have landed to Mars!')
elif teleport == 1:
    print('You have landed to Venus!')
else:
    print('You have landed to Jupyter')

print('Great job, here is the team.')
print('Jack, Jenny, Max')

characters = ['Jack', 'Jenny', 'Max']
print(' Great job, here is the team:')
print(', '.join(characters))

character_pick = input('Choose your character: ').strip().title()
if character_pick in characters:
    print(f'You have chosen {character_pick}!')
else:
    print('Invalid character selected. Exiting game.')
    sys.exit()