# Store the input rucksacks in a list
# rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
#              'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#              'PmmdzqPrVvPwwTWBwg',
#              'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#              'ttgJtRGJQctTZtZT',
#              'CrZsJsPPZsGzwwsLwLmpwMDw']
rucksacks = []
with open('data3.txt') as f:
    for line in f:
        rucksacks.append(line.strip())
# Initialize a variable to store the sum of priorities
priorities_sum = 0
print(ord('a')) #97
print(ord("A")) #65 


print(ord('a') - 96)
print(ord('A') - 38)
# Iterate over the rucksacks
for rucksack in rucksacks:
  # Get the length of the rucksack
  length = len(rucksack)
  
  # Get the first half of the rucksack
  first_half = rucksack[:length // 2]
  
  # Get the second half of the rucksack
  second_half = rucksack[length // 2:]
  
  # Initialize a set to store the common item types
  common_item_types = set()
  
  # Iterate over the first half of the rucksack
  for item in first_half:
    # Check if the item is also in the second half
    if item in second_half:
      # Add the item to the set of common item types
      common_item_types.add(item)
      
  
  # If there is only one common item typ
  for item in common_item_types:
    priority = ord(item)
    if priority >= 97:
        priority -= 96
    else:
        priority -= 38
    priorities_sum += priority
# Print the sum of priorities
print(priorities_sum)
