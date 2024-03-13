filenames = ["document", "report", "presentation"]
for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}.txt"
    print(row)



ips = ['100.122.133.105', '100.122.133.111']


user_choice = int(input("Enter the index of the Ip you want:") )

messege = f"You chose {ips[user_choice]}"
print(messege)

#Excercose2
temperatures = [10.5, 15, "string_as_numbers"]
print(temperatures)
#ex5 remove an item from the list seconds
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
print(seconds)

#excercise 3 for day 5, finding menu
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")


