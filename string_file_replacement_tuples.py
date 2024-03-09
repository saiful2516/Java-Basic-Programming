filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename  in  filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

#Tuple does not support repalce or append method because it does not allow item to be changed.
#so list is more flexible than tuples. so list is more popular than tuples.

tuplenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
for tuplename in tuplenames:
    print(tuplename)