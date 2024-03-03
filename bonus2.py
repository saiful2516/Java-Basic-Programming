password = input("Enter password: ")
while password != "pass123":
    password = input("Enter password: ")
print("Password was correct!")

x = 1
while x<= 6:
    print(x)
    x = x + 1

while True:
    print("Hello".lower())



 x = 1
 while x > 2:
     print("yes")
 #Nothing will be printed out.

 #excercise:

x = 1
y = 2
z = 3
print(x, y, z)

#excercise 2:
Capital = input("Enter your name:")
#while True:
print(Capital.capitalize())



while True:
    name = input("Enter your name:")
    print(name.capitalize())

#Upper case letter function.
while True:
    name = input("Enter your name:")
    print(name.upper())


countries = []
while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)