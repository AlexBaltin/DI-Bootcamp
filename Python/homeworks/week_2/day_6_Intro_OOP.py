# ----------------------------------------------------------Exercise 1: Cats-----------------------------------------------
# 
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# susan = Cat("Susan", 15)
# # print(susan.age, susan.name)
# basbusa = Cat("Basbusa", 5)
# koshka = Cat("Koshka", 25)

# def get_oldest_cat(cats):
#     oldest_cat = cats[0]

#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat

# my_cats = [susan, basbusa, koshka]
# oldest_cat_result = get_oldest_cat(my_cats)
# print(f"The oldest cat is {oldest_cat_result.name}, and is {oldest_cat_result.age} years old")
# 
# ----------------------------------------------------------Exercise 2: Dogs-----------------------------------------------
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof")
    
#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm high!")

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

# dogs = ["Rex", "Teacup"]

# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
# ----------------------------------------------------------Exercise 3: Who’s the song producer?-----------------------------------------------
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for lyrics in self.lyrics:
#             print(lyrics)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# lyrics = stairway.lyrics
# print(lyrics)

# stairway.sing_me_a_song()
# ----------------------------------------------------------Exercise 4 : Afternoon at the Zoo-----------------------------------------------
# class Zoo:
#     def __init__(self, zoo_name):
#         self.animals = []
#         self.zoo_name = zoo_name

#     def add_animal(self, new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#         else:
#             print(f"You already added a {new_animal}")

#     def get_animals(self):
#         print("List of animals in the zoo: ", self.animals)

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#         else:
#             print(f"{animal_sold} is already sold")

#     def sort_animals(self):
#         sorted_animals = sorted(self.animals)
        


        


# zoo = Zoo("Alex's Zoo")

# zoo.add_animal("Snake")
# zoo.add_animal("Horse")
# zoo.add_animal("Tiger")
# zoo.add_animal("Llama")
# zoo.add_animal("Leon")
# zoo.add_animal("Alligator")
# zoo.add_animal("Turkey")

# zoo.get_animals()

# zoo.sell_animal("Horse") 

# zoo.get_animals()  

# zoo.sell_animal("Elephant") 

# zoo.sort_animals()
# 
# 
# # -----------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------Exercises XP Ninja-------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------

# class Phone:
#     def __init__(self, phone_number):
        
#         self.phone_number = phone_number
#         self.call_history = []
#         self.messages = []

#     def call(self, other_phone):
        
#         call_info = f"{self.phone_number} called {other_phone.phone_number}"
#         print(call_info)

#         self.call_history.append(call_info)

#         other_phone.call_history.append(f"{other_phone.phone_number} got a call from {self.phone_number}")

#     def show_call_history(self):

#         if len(self.call_history) == 0:
#             print("The history is empty.")
#         else:
#             print("The history of calls:")
#             for call in self.call_history:
#                 print(call)

#     def send_message(self, other_phone, content):

#         message = {
#             'to': other_phone.phone_number,
#             'from': self.phone_number,
#             'content': content
#         }
#         print(f"A messege from {self.phone_number} to {other_phone.phone_number}: {content}")

#         self.messages.append(message)
#         other_phone.messages.append(message)

#     def show_outgoing_messages(self):

#         if len(self.messages) == 0:
#             print("No outgoing messages.")
#         else:
#             print("Outgoing messages:")
#             for message in self.messages:
#                 if message['from'] == self.phone_number:
#                     print(f"To: {message['to']}, content: {message['content']}")

#     def show_incoming_messages(self):

#         if len(self.messages) == 0:
#             print("No incoming messages.")
#         else:
#             print("Incoming messages:")
#             for message in self.messages:
#                 if message['to'] == self.phone_number:
#                     print(f"From: {message['from']}, content: {message['content']}")

#     def show_messages_from(self, other_phone):

#         if len(self.messages) == 0:
#             print("No messages.")
#         else:
#             print(f"Message from {other_phone.phone_number}:")
#             for message in self.messages:
#                 if message['from'] == other_phone.phone_number:
#                     print(f"To: {message['to']}, content: {message['content']}")

# phone1 = Phone("123-456-7890")
# phone2 = Phone("987-654-3210")

# phone1.call(phone2)

# phone1.send_message(phone2, "Hi!")
# phone2.send_message(phone1, "Helloooooo!")

# phone1.show_call_history()
# phone2.show_call_history()

# phone1.show_outgoing_messages()
# phone1.show_incoming_messages()
# phone2.show_outgoing_messages()
# phone2.show_incoming_messages()

# phone1.show_messages_from(phone2)
# phone2.show_messages_from(phone1)