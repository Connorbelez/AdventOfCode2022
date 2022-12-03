def find_common_item_type(ruck_sacks):
    common_item_type = []
    for ruck_sack in ruck_sacks:
        first_compartment = ruck_sack[:len(ruck_sack) // 2]
        second_compartment = ruck_sack[len(ruck_sack) // 2:]
        for item in first_compartment:
            if item in second_compartment:
                common_item_type.append(item)
                break
    return common_item_type

def find_badge_item_type(groups):
    badge_item_type = []
    for group in groups:
        common_items = set(group[0]) & set(group[1]) & set(group[2])
        badge_item_type.append(common_items.pop())
    return badge_item_type

def compute_priority(item_type):
    priority = 0
    for item in item_type:
        if item.isalpha():
            if item.islower():
                priority += ord(item) - 96
            else:
                priority += ord(item) - 38
    return priority

ruck_sacks = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
common_item_type = find_common_item_type(ruck_sacks)
priority = compute_priority(common_item_type)
print("The sum of the priorities of the item types that appear in both compartments of each rucksack is:", priority)

groups = [["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"], ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]]
badge_item_type = find_badge_item_type(groups)
priority = compute_priority(badge_item_type)
print("The sum of the priorities of the item types that corresponds to the badges of each three-Elf group is:", priority)


with open("data3.txt") as f:
    data = f.readlines()
    #data = [["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"], ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]]
    prev = 0
    groups = [data[i:i + 3] for i in range(0, len(data), 3)]
    #groups = [["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"], ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]]
    pt = 0
    for group in groups:
        ci = compute_priority(find_badge_item_type(groups))
        priority = ci
        if priority >= 97:
            priority -= 96
        else:
            priority -= 38
        pt += priority
    print(pt)
        