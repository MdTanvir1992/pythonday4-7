# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
# my_life_remaing_year = 90 - int(age)
# # Write your code below this line 👇
# my_l_m = my_life_remaing_year * 12
# my_l_w = my_life_remaing_year * 52
# my_l_d = my_life_remaing_year * 365
# print(f" You have left {my_life_remaing_year} Year\n You have left {my_l_m} Month\n You have left {my_l_w} Week\n You have left {my_l_d} Days\n")

#
# print("Welcome to the tip calculator.")
# bill = input("What was the total bill?")
# tip = input("What percentage tip would you like to give?")
# person = input("How many people to split the bill?")
# total_tip = float(bill) * int(tip)
# total_tip /= 100
# total_bill = total_tip + float(bill)
# per_person = round(total_bill / int(person),2)
# per_person = "{:.2f}".format(per_person)
# print(f"Each person should pay: {per_person}")

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 1
# for number in range(2, 101, 2):
#     total += number
#
# print(total)
#
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# for number in range(1, 101):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#         continue

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


