import csv

f = open('test.csv', 'w')

i =  input()
a =[]
for a in range(int(i)):
    b =  input()    
    a.append(i)

with f:
    writer = csv.writer(f) 
    for row in a:
        writer.writerow(row)
f.close()
f = open('test.csv', 'r')
with f:

    reader = csv.reader(f)

    for row in reader:
        for e in row:
            print(e)