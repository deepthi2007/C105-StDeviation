import csv
import math
import statistics

with open("data.csv",newline='') as f:
    reader = csv.reader(f)
    read1 = list(reader)
    read2 = read1.pop(0)
    data=[]
    for i in read2 :
        data.append(int(i))
    """ Mean """
    sum = 0
    for i in data :
        sum=sum+i
    mean = sum/len(data)
 
    """ STD DEV """
    squares = []
    for i in data :
        sum2 = i-mean
        squares.append(sum2**2)
    sum3 = 0
    for i in squares :
        sum3=sum3+i
    result = sum3/(len(data)-1)
    stdev1 = math.sqrt(result)

    stdev2 = statistics.stdev(data)

    print("Real St-Deviation -> ",stdev1)
    print("Calcualted St-Dev -> ",stdev2)