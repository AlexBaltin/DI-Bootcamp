
# -------------------------------------------------------Exercise1-What are you learning-----------------------------------
# 
# def display_message():
#     print("I'm learning OOP")

# display_message()
# prints "I'm learning OOP"

# -------------------------------------------------------Exercise2-Whats your favourite book-----------------------------------
# 
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")

# favorite_book("Alice in Wonderland")
#   prints "One of my favorite books is Alice in Wonderland"
# -------------------------------------------------------Exercise3-Some geography-----------------------------------
# 
# def describe_city(city, country):
#     print(f"{city} is in {country}")
# describe_city("Ramat-Gan", "Israel")
#                                                
# 
# -------------------------------------------------------Exercise4-Random-----------------------------------
# 
# import random

# def random_number(accepted_intenger):

#     random_intenger = random.randint(1, 100)

#     if accepted_intenger == random_intenger:
#         print(f"success {accepted_intenger}, {random_intenger}")
#         return True
#     else:
#         print(f"failed {accepted_intenger}, {random_intenger}")
#         return False

# while True:
#     is_same = random_number(3) 
#     if is_same == True:
#         break
# -------------------------------------------------------Exercise5-Let’s create some personalized shirts !-----------------------------------

# def make_shirt(size = "large", text = "I love Python"):
#     if size == "small":
#         size = "S"
#     if size == "medium":
#         size = "M"  
#     if size == "large":
#         size = "L"


#     print(f"The size of the shirt is {size} and the text is {text}")


# make_shirt()
# make_shirt("medium")
# make_shirt("small", "LOL")
# make_shirt(size="large", text="hello")
# make_shirt(text="hello", size="medium")
# -------------------------------------------------------Exercise6-Magicians -----------------------------------


# def show_magicians(magician_names):
#     for name in magician_names:
#         print(name)

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] = "the Great " + magician_names[i]
        


# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


# show_magicians(magician_names)
# make_great(magician_names)
# show_magicians(magician_names)

# -------------------------------------------------------Exercise7-Temperature Advice -----------------------------------

# import random

# def get_random_temp():
#     return random.randint(-10,40)

# random_number = get_random_temp()
# print(f"random temperature: {random_number}")

# def main(temperature):
#     for hystory_of_temperature in temperature:
#         
    

# temperature = []
# print(temperature)
