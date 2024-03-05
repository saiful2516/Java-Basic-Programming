country = "India"

match country:
    case 'USA':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")

members = ["john smith", "sen plakay", "dora ngacely"]

for item in members:
    item = item.title()
    print(item)

colors = [11, 34, 98, 43, 45, 54, 54]
for item in colors:
    print(item)