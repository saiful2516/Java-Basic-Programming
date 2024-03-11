filenames = ["document", "report", "presentation"]
for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}.txt"
    print(row)


ips = ['100.122.133.105', '100.122.133.111']

user_option = int(input("Enter the index of the Ip you want:") )

match user_option:
     case 1 :
         for index, item in enumerate(ips):
             print("You chose", item)

     case 2 :
         for index, item in enumerate(ips):
             print("You chose", item)




