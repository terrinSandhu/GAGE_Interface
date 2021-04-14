import csv
import numpy as np

#numpy method
file = open("test.csv")
numpy_array = np.loadtxt(file, delimiter=",")

print(numpy_array)



#csv brute force method
datafile = open('test.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
    data.append(row)    
print (data[1:4])