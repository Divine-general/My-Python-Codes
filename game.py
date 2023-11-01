##lets create a fizbuzz game
## i'm a genius
##lets begin
print('Begin Game')


## create a variable to store number
number:int = int(input("Enter a number:  "))


if number % 3 == 0 and number % 2 == 0:
    print("FIZZBUZZ")


# elif number % 3 == 0 and number % 2 == 0:
#     print("FIZZBUZZ")

elif number % 2 == 0:
    print("FIZZ")

elif number % 3 == 0:
     print("BUZZ")

else:
     print(number)




