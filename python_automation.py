import os
import datetime
import csv

file = os.path.getmtime('file_lists.txt')
print(file)

time = datetime.datetime.fromtimestamp(file)
print(time)

print(os.name)

f = open('SQL queries.txt')
csv_f = csv.reader(f)
for row in csv_f:
    print(row)

# with open('SQL queries.txt', 'w') as file:
#     writable = csv.writer(file)
#     writer.writerows('SQL queries')

# for line in 