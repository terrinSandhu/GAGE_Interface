import csv

filename = 'test_driver.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if  len(row[1]) == 1:
            print(row[0])

