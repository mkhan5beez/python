
# importing  all the
# functions defined in test.py
from FirstTest import *
 
# calling functions
hello()

#reading File
with open('Data/orderhistory.csv') as f:
    filecounter = f.read()
    print(filecounter)