# take a number from the user and print the number if even or odd

# number = int(input("Enter a number: "))
# if number % 2 == 0 and number > 20:
#     print("Ther number is even")
#     print("The number is greater than 20")
# else:
#     print("Ther number is odd.")
#     print("The number is not greater than 2020")
# print("Hello Coding")
indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "ristto"]

dish = input("Enter a dish name: ")
if dish in indian:
    print("The dish is indian")
elif dish in chinese:
    print("The dish is chinese")
elif dish in italian:
    print("The dish is italian")
else:
    print("The dish is not in the menu")
    print("We are sorry sir!!")
