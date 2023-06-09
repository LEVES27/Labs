from num2word import word

# Виводимо привітання
print("Hello!")

"""Asks for user integer num"""
# Запитуємо користувача про ціле число
num = input("Enter your number: ")

"""Prints user number as text"""
# Виводимо число користувача у текстовому форматі
print("Your number is: " + word(num))
