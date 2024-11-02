my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# print(my_list)

cars = ["Tesla", "Mclauren", "Bugatti", "Chevrolet", "Renault", "Audi", "Subaru"]

choice = cars[-6], cars[3]

cars[6] = "ferrari"  # replace the element with index number 6 with "ferrari"
cars.append("Toyota")  # add the element to the of the list
cars.insert(0, "BMW")  # add the new element to the index number specified
cars.remove("Toyota")  # to remove from the list
cars.pop()  # to remove from the back list with the index number
del cars[6]
# print(cars)


# print(f"I want chop life make i buy 3 {cars[1]}")
# print(choice)

firstname = "muhydeen"
lastname = "dogbajale"

fullname = firstname + " " + lastname
# print(fullname)

firstname = "muhydeen"
lastname = "dogbajale"
middlename = "ola"

age = 19

# fullname = firstname + " " + middlename + " " + lastname
# print(f"{fullname} is {age} years old")

"""assessment

====
create a list called guest_list. your list should contain atleast 3 people you want to invite to dinner.
print a message to each guest telling them they are invited
"""

guest_list = ["ayo", "wale", "yomi"]
guest_list[2] = "muhy"
guest_list.insert(0, "ola")
guest_list.append("femi")
guest_list.insert(3, "simbi")

guest_list.remove("wale")

guest_list.pop(0)

del guest_list[1]


# print(f"{guest_list[0]} is invited to dinner")
# print(f"{guest_list[1]} is invited to dinner")
# print(f"{guest_list[2]} is invited to t dinner")
# print(f"{guest_list[3]} is invited to the dinner")
# print(f"{guest_list[4]} is invited to the dinner")
# print(f"{guest_list[5]} is invited to the dinner")

food_items = ["rice", "meat", "thyme", "onion", "salt", "yam", "curry"]
food_items.sort(reverse=True)
food_items.sort()
sorted_items = sorted(food_items)

# print(sorted_items)
# print(food_items)

"""list organizing"""
# guests = ["ola", "muhydeen", "omolara", "faruk", "ekenne", "emeka", "ife", "zainab"]

# for guest in guests:
    # print(f'{guest}, you are invited to dinner')


fruits = ["watermelon", "apple", "grape"]

# for fruit in fruits:
     # print(f"{fruit}")

# numbers = list(range(0, 100))
# print(numbers)

# for number in range(1, 100, 2)
   # print(number)

# for number in range(1, 21):
   # print(number)

players = ["maguire", "fernandes", "ronaldo", 'fred', "pogba", "rashford", "sancho"]

star_players = players[1:4]  # slicing our list of players

for player in star_players:
    print(player)