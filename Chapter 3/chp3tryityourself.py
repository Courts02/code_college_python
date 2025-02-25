names = ["Tristen", "Megan", "Leah", "Ben"]

for name in names:
    print(f"Hey, {name}!! How are you?")

transportation = ["Porsche GT3 RS", "Golf 8R", "Yamaha YZF-R1M", "Kawasaki ZX-10R", "KTM 1390 Super Duke R"]

for model in transportation:
    print(f"I would like to own a {model}!")

guests = ["Mom", "GrandFather", "Pops", "Friend"]

for guest in guests:
    print(f"Dearest {guest}, \nI would be more than delighted to have you over for dinner. Would you be so kind to join me please?\n")   
    print(f"Unfortunately, {guests[2]} can't make it to the dinner.\n")
    guests[2] = "Cousins"

for guest in guests:
    print(f"Dearest {guest}, \nI would be more than delighted to have you over for dinner. Would you be so kind to join me please?\n")

    print("I found a bigger table, so I can invite more guests!\n")

guests.insert(0, "Tristen")
# add a guest in the middle of the list:
guests.insert(1, "Megan")

guests.append("Nothando")

for guest in guests:
    print(f"Dearest {guest}, \nI would be more than delighted to have you over for dinner. Would you be so kind to join me please?\n")
    print("I just found out that my new dinner table won't arrive in time. I can only invite two people for dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"I'm sorry, {removed_guest}, but I can't invite you to dinner.\n")

for guest in guests:
    print(f"Dear {guest}, \nYou are still invited to dinner! Looking forward to seeing you\n")

del guests[:]


# List of places to visit (not in alphabetical order)
places = ["Tokyo", "Paris", "Japan", "Stockholm", "New York"]

# Step 1: Print the list in its original order
print("Original list:")
print(places)

# Step 2: Print the list in alphabetical order without modifying the original list
print("\nSorted list (alphabetical):")
print(sorted(places))

# Step 3: Show that the original list is still in its original order
print("\nOriginal list after sorted():")
print(places)

# Step 4: Print the list in reverse-alphabetical order without modifying the original list
print("\nSorted list (reverse alphabetical):")
print(sorted(places, reverse=True))

# Step 5: Show that the original list is still in its original order
print("\nOriginal list after reverse sorted():")
print(places)

# Step 6: Reverse the list using reverse()
places.reverse()
print("\nList after reverse():")
print(places)

# Step 7: Reverse the list again to return to the original order
places.reverse()
print("\nList after reversing back to original order:")
print(places)

# Step 8: Sort the list in alphabetical order using sort()
places.sort()
print("\nList after sort() in alphabetical order:")
print(places)

# Step 9: Sort the list in reverse-alphabetical order using sort()
places.sort(reverse=True)
print("\nList after sort() in reverse alphabetical order:")
print(places)

guests = ["Mom", "GrandFather", "Tristen", "Megan", "Cousins"]
print(f"Number of people invited to dinner: {len(guests)}")

countries = ["Japan", "France", "Brazil", "Canada", "India"]

countries.append("Australia")

countries.insert(0, "Germany")

countries.remove("Brazil")

popped_country = countries.pop()
print(f"Removed country with pop(): {popped_country}")

countries.sort()

countries.reverse()

print(f"Number of countries in the list: {len(countries)}")

del countries[1]

print("Final list of countries:")
print(countries)