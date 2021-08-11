#reading File
with open('Data/orderhistory.csv') as f:
    filecounter = f.read()
    print(filecounter)

    f.close()

#Reading CSV
import csv
