import csv

file = open('test.csv', 'r')
csvReader = csv.reader(file)

dataX=[]
dataY=[]
for row in csvReader:
    print(row)
    #dataX.append([1.0] + row[:-1])
    #dataY.append(row[-1])
file.close()
    #print(row)