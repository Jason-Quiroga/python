
if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']

    spam_str = ''


def item_list(some_list):
    item_string = ''
    length = len(some_list)  # Find the length of the list

    counter = 0  # Set the counter to 0
    for item in some_list:
        if counter == length - 1:  # If it's the last item, add the word 'and'
            item_string = item_string + 'and ' + item
        else:  # If it's not the last item, add a comma
            item_string = item_string + item + ', '
        counter += 1
    return item_string


"""
for spam_item in spam:
    print("Spam item: " + spam_item)
    spam_str = spam_str + spam_item
    print("Spam str: " + spam_str)

print(spam_str)
"""

# Spam list
spam_str = (item_list(spam))
print(spam_str)


# Cities list
cities = ['New York', 'Chicago', 'Atlanta', 'Burlington', 'Philadelphia', 'Denver']
cities_str = (item_list(cities))
print(cities_str)

# Food list
food = ['carrots', 'mango', 'avocado']
food_str = (item_list(food))
print(food_str)
