# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------Exercises XP--------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------Exercise 1 : Favorite Numbers-----------------

# my_fav_numbers = {17, 27, 30}

# my_fav_numbers.add(20)
# my_fav_numbers.add(15)

# my_fav_numbers.remove(17)

# friend_fav_numbers = {5, 7, 33}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# print("My Favorite Numbers:", my_fav_numbers)
# print("Friend's Favorite Numbers:", friend_fav_numbers)
# print("Our Favorite Numbers:", our_fav_numbers)

# ------------------Exercise 2: Tuple-----------------------------
# ------------------------------------------------------------------------Exercise 3: List------------------------------
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")

# apples_total = basket.count("Apples")
# print(f"There are {apples_total} apples in the basket.")

# basket.clear()

# ------------------Exercise 4: Floats----------------------------

# ------------------------------------------------------------------------Exercise 5: For loop--------------------------

# for number in range(1, 21):
#     print(number)

# numbers = list(range(1, 21))


# for index in range(len(numbers)):
#     if index % 2 == 0:  
#         print(numbers[index])

# ------------------------------------------------------------------------Exercise 6: while Loop------------------------
# my_name = "Alex"
# user_name = None
# while my_name != user_name:
#     user_name = input("What is your name? :")
#     print("Nice to meet you")
    
# else:
#     print("Lol")

# ------------------------------------------------------------------------Exercise 7: Favorite fruits--------------------

# user_fav_fruirs = input("What is your favorite fruit/fruits? example: apple mango cherry..... :")
# user_fav_fruirs = user_fav_fruirs.split()

# chosen_fruit = input("Choose the fruit: ")

# if chosen_fruit in user_fav_fruirs:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# ------------------------------------------------------------------------Exercise 8: Who ordered a pizza ?--------------
# toppings = []

# pie_price = 10
# topping_price = 2.5

# while True:
#     topping = input("Choose the topping or type quit for quit:")
    
#     if topping == 'quit':
#         break
    
#     toppings.append(topping)
#     print(f"You`ll add {topping} to your pizza.")


# total_price = pie_price + (topping_price * len(toppings))


# print("Your pizza will be with those toppings:")
# for topping in toppings:
#     print(f"- {topping}")

# print(f"Full price: {total_price}")

# ------------------------------------------------------------------------Exercise 9: Cinemax----------------------------

# total_cost = 0

# while True:
#     age_input = input("What is your age? (exit to exit): ")
#     if age_input.lower() == 'exit':
#         break
     
#     age = int(age_input)
    
#     if age < 3:
#         price = 0
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 15
    
#     total_cost += price

# print(f"Final price: ${total_cost}")

# names = ["Alex", "Max", "Andrew", "Kate"]
# allowed_names = []

# for name in names:
#     age_input = input(f"What is the age of {name}?: ")
#     age = int(age_input)
    
#     if age < 16 or age > 21:
#         allowed_names.append(name)
#     else:
#         print(f"{name} is not allowed to watch this movie.")

# print("Final list:")
# for name in allowed_names:
#     print(name)

# ------------------------------------------------------------------------Exercise 10 : Sandwich Orders----------------------------

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# finished_sandwiches = []


# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")
   
# i = 0  
# while i < len(sandwich_orders):
#     sandwich = sandwich_orders[i] 
#     finished_sandwiches.append(sandwich)
#     i += 1  


# for sandwich in finished_sandwiches:
#     print(f"I made your {sandwich}")

# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------Exercises XP Gold---------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------Exercise 1 : Concatenate Lists---------------------------

# names_1 = ["Alex", "Max", "Andrew"]
# names_2 = ["Ayelet", "Einav", "Kevin"]

# names_1.extend(names_2)

# print(names_1)

# ------------------------------------------------------------------------Exercise 2: Range of numbers-----------------------------

# for number in range(1500, 2500):
#     if number % 5 == 0 and number % 7 == 0 :
#         print(number)

# ------------------------------------------------------------------------Exercise 3: Check the index------------------------------

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name = input("Whats your name?  :")

# if user_name in names:
#     num = names.index(user_name)
#     print(f"if input is {user_name} we should be printing index {num}")
# else:
#     print("Lol")

# ------------------------------------------------------------------------Exercise 4: Greatest Number------------------------------
# num_1 = int(input("1st number is: "))
# num_2 = int(input("2nd number is: "))
# num_3 = int(input("3rd number is: "))

# if num_1 >= num_2 and num_1 >= num_3:
#     greatest_num = num_1

# elif num_2 >= num_1 and num_2 >= num_3:
#     greatest_num = num_2

# else:
#     greatest_num = num_3

# print(f"The greatest number is: {greatest_num}")

# ------------------------------------------------------------------------Exercise 5: The Alphabet---------------------------------

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# vowels = 'aeiou'

# for letter in alphabet:
#     if letter in vowels:
#         print(f"'{letter}'-vowel.")
#     else:
#         print(f"'{letter}'-consonant.")

# ------------------------------------------------------------------------Exercise 6: Words and letters-----------------------------
# words = []
# for user_word in range(7):
#     word = input("Enter a word: ")
#     words.append(word)

# letter = input("Enter a single character: ")


# if len(letter) != 1:
#     print("Error: Please enter exactly one character.")
# else:
#     for word in words:
#         if letter in word:
#             index = word.index(letter)
#             print(f"In the word '{word}', the letter '{letter}' first appears at index {index}.")
#         else:
#             print(f"The letter '{letter}' is not found in the word '{word}'.")
# ------------------------------------------------------------------------Exercise 7: Min, Max, Sum---------------------------------

# list_of_numbers = range(1, 1000001)


# print("Minimum value:", min(list_of_numbers))
# print("Maximum value:", max(list_of_numbers))

# total_sum = sum(list_of_numbers)
# print("Total sum:", total_sum)

# ------------------------------------------------------------------------Exercise 8 : List and Tuple-------------------------------

# user_input = input("Your numbers: ")

# user_list = list(user_input.split(","))
# user_tuple = tuple(user_input.split(","))
# print(user_list, "\n", user_tuple)

# ------------------------------------------------------------------------Exercise 9 : Random number--------------------------------
# import random

# won_times = 0
# loose_times = 0

# while True:
    
#     user_input = input("Enter a number from 1 to 9: ")

#     if user_input == "exit":
#         print(f"you won {won_times} times and loose {loose_times}")
#         print("bye")
#         break

#     user_input = int(user_input)


#     random_input = random.randint(1,9)

#     if user_input == random_input:
#         won_times += 1
#         print("Winner")
#     else:
#         loose_times += 1
#         print("Better luck next time times")
    