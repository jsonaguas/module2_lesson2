# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

# The first elif statement should use double '=' to indicate comparison. The
# statement after else is redundant and can be removed.

#Corrected Code:
number = input("Enter a number: ")
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
