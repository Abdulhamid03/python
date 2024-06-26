cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Boston']


# for city in cities:
#     print(city)

# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
# for index in range(len(cities)):
#     print("Current index: ", index, '| Current city: ', cities[index])

# set a empty list
# while the length of the lsit is less than 5 
# ask user to enter a city name
# before appending the city to the list, check if the city exists

# user_input = []

# while len(cities) <= 5:
#     usr_input = input("please enter your city name: ")
#     if usr_input in cities:
#         print("city already exists:", usr_input)
#         break
#     else:
#         cities.append(usr_input)

#     print(len(cities), cities)






# spendigs = [32.45, 18.65, 23.45, 78.32, 5.23]

# sum = 0.0
# for spending in spendigs:
#     sum += spending
# print('Money spent:', sum)



# spendigs.sort(reverse=True)
# print(spendigs)

## copying list
original_list = [1, 2, 3, 4, 5]
new_list = original_list

new_list.append(6)

print(new_list)
print(original_list)

    