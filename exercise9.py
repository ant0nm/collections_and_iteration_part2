def print_list(l):
    for item in l:
        print('*', item)

grocery_list = ['milk', 'eggs', 'turkey', 'butter', 'salmon',
'almonds', 'apples', 'hummus', 'toiler paper']

print()
print_list(grocery_list)

grocery_list.append('rice')

print()
print_list(grocery_list)

print()
print("You need to pick up {} things at the grocey store today.".format(len(grocery_list)))

print()
if 'bananas' in grocery_list:
    print("You need to pick up bananas.")
else:
    print("You don't need to pick up bananas today.")

print()
print("The second item on your grocery list is {}.".format(grocery_list[1]))

grocery_list.sort()

print()
print_list(grocery_list)

print()
print("They're out of salmon today, so cross it off your list!")
grocery_list.remove('salmon')
print_list(grocery_list)
