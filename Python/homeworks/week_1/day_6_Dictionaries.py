# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------Exercises XP--------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------Exercise 1: Convert lists into dictionaries---

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# something = {}
# for key, value in zip(keys, values):
#     something[key] = value


# print(something)

# ------------------------------------------------------------------------Exercise 2 : Cinemax #2-----------------------

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# age = 0
# price1 = 0
# price2 = 10
# price3 = 15
# total = 0
# if age > 3 and age < 12:
#     price = price2
#     print("10$")
# if age > 12:
#     price = price3
#     print("15$")

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# prices = {}
# total_price = 0
# for each_person_name in family:
#     age = family[each_person_name]
    

#     if age < 3:
#         price = 0
    
#     if age >= 3 and age <= 12:
#         price = 10

#     if age > 12:
#         price = 15

#     prices[each_person_name + " needs to pay"]=price

#     total_price = total_price + price

# print(prices)
# print(total_price)

# ------------------------------------------------------------------------Exercise 3: Zara------------------------------

# brand = {
#     "name":"Zara", 
#     "creation_date":1975,
#     "creator_name":"Amancio Ortega Gaona",
#     "type_of_clothes":['men','women',"children","home"],
#     "international_competitors":["Gap","H&M","Benetton"],
#     "number_stores":7000,
#     "major_color":{
#         "France":["blue"],
#         "Spain":["red"],
#         "US":["pink","green"]
#     }
# }
# brand["number_stores"]=2
# # print("Zaras clients are: " + str(brand["type_of_clothes"]))
# print("Zaras clients are: " + "; ".join(brand["type_of_clothes"]))
# brand["country_creation"]="Spain"
# if "international_competitors" in brand:
#     brand["international_competitors"] = brand["international_competitors"] + ["Desigual"]
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(",".join(brand["major_color"]["US"]))
# print(len(brand))
# print(brand.keys())
# more_on_zara = {
#     "creation_date": 1975, 
#     "number_stores": 10000
# }
# brand.update(more_on_zara)
# print(brand)
# print(brand["number_stores"])

# ------------------------------------------------------------------------Exercise 4 : Disney characters----------------

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users_A = {}
# xA = 0
# # for x, eachuser in enumerate(users):
# #   disney_users_A[eachuser] = x
# for eachuser in users:
#     disney_users_A[eachuser] = xA
#     xA += 1
    
# print(disney_users_A)


# disney_users_B = {}
# xB = 0
# for eachuser in users:
#     disney_users_B[xB] = eachuser
#     xB += 1
# print(disney_users_B)

# disney_users_C = {}
# xC = 0
# for eachuser in sorted(users):
#     disney_users_C[eachuser] = xC
#     xC += 1
# print(disney_users_C)

# disney_users_D = {}
# xD = 0
# for eachuser in users:
#     if "i" in eachuser:
#         disney_users_D[eachuser] = xD
#         xD += 1
# print(disney_users_D)

# disney_users_E = {}
# xE = 0
# for eachuser in users:
#     if eachuser.startswith("M") or eachuser.startswith("P"):
#         disney_users_E[eachuser] = xE
#         xE += 1
# print(disney_users_E)


# --------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------Exercises XP Plus---------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------Exercise 1 : Student Grade Summary------------

# my_dict = {}

# for key in my_dict:
#     value = my_dict[key]

# for key, value in my_dict.items():
#     pass

# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72],
#     # "Alex": [89.5, 89.5, 89.5]
# }

# student_averages = {}
# for student in student_grades:
#     grades = student_grades[student]
#     average = sum(grades) / len(grades)
#     student_averages[student] = average
# print(student_averages)
# # {'Alice': 93.33333333333333,
# #  'Bob': 77.66666666666667, 
# # 'Charlie': 89.0, 
# # 'Dana': 87.66666666666667, 
# # 'Eli': 76.66666666666667}

# student_letter_grades = {}
# for student in student_averages:
#     average = student_averages[student]
#     if average >= 90:
#         student_letter_grades[student] = "A"
#     if average >= 80 and average <= 89:
#         student_letter_grades[student] = "B"
#     if average >= 70 and average <= 79:
#         student_letter_grades[student] = "C"
#     if average >= 60 and average <= 69:
#         student_letter_grades[student] = "D"
#     if average < 60:
#         student_letter_grades[student] = "F"

# print(student_letter_grades)


# class_average = sum(student_averages.values()) / len(student_averages)
# print(class_average)


# for student in student_letter_grades:
#     average = student_averages[student]
#     letter_grade = student_letter_grades[student]
#     print(student, average, letter_grade)


#     # print(f"My name {student}, my average is {average}")

# ------------------------------------------------------ Exercise 2 : Advanced Data Manipulation and Analysis------------

# sales_data = [
#     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
#     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
#     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
#     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
#     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
#     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
#     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
# ]

# total_sales = {}

# for sale in sales_data:
#     product = sale["product"]
#     price = sale["price"]
#     quantity = sale["quantity"]
#     total_amount = quantity * price
    
#     if product in total_sales:
#         total_sales[product] += total_amount
#     else:
#         total_sales[product] = total_amount

# print(total_sales)

# customer_spending_profile = {}

# for sale in sales_data:
#     customer = sale["customer_id"]
#     price = sale["price"]
#     quantity = sale["quantity"]
#     each_customer_spending_profile = quantity * price 

#     if customer in customer_spending_profile:
#         customer_spending_profile[customer] += each_customer_spending_profile
#     else:
#         customer_spending_profile[customer] = each_customer_spending_profile

# print(customer_spending_profile)

# for sale in sales_data:
#     sale["Total_price"] = sale["quantity"] * sale["price"]

# print(sales_data)

# high_value_transactions = sorted(
#     [transaction for transaction in sales_data if transaction["Total_price"] > 500],
#     key=lambda x: x["Total_price"],
#     reverse=True
# )

# print("High-Value Transactions:", high_value_transactions)

