houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0,
}

def get_input(prompt, options):
  while True:
    try:
      answer = int(input(prompt))
      if 1 <= answer <= options:
        return answer
      else:
        print(f"Please enter a number between 1 and {options}.")
    except ValueError:
      print('Please enter a valid number.')



Q1 = get_input('Do you like Dawn and Dusk? 1) Dawn 2) Dusk ', 2)
if Q1 == 1:
  houses["Gryffindor"] += 1
  houses["Ravenclaw"] += 1
elif Q1 == 2:
    houses['Hufflepuff'] += 1
    houses['Slytherin'] += 1

Q2 = get_input('When I am dead, I want people to remember me as 1. The Good 2. The Great 3. The Wise 4. The bold: ', 4)

if Q2 == 1:
  houses['Hufflepuff'] += 2
elif Q2 == 2:
  houses['Slytherin'] += 2
elif Q2 == 3:
  houses['Ravenclaw'] += 2
elif Q2 == 4:
  houses['Gryffindor'] += 2

Q3 = get_input('Which kind of instrument most pleases your ear 1. The violin 2. The trumper 3. The piano 4. The drum: ', 4)

if Q3 == 1:
  houses['Slytherin'] += 4
elif Q3 == 2:
  houses['Hufflepuff'] += 4
elif Q3 == 3:
  houses['Ravenclaw'] += 4
elif Q3 == 4:
  houses['Gryffindor'] += 4

print('\nFinals scores')
for house, score in houses.items():
  print(f'{house}: {score}')

# Determine the house with the highest score
max_score = max(houses.values())
winners = [house for house, score in houses.items() if score == max_score]
print('\nYou belong to:', ', '.join(winners))
