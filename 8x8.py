##8X8 Checker - checks for number of calls and minutes used in a CSV file.
##Col 0 is the first one. Col 3 is the Minutes, Col4 dial from number, Col5 dial to
##Download the file from the billing area of 8x8. 
##Alvaro Gil 2014-03-19

import csv
import os
import sys
import string

infile="8x8in.txt"
outfile="8x8out.txt"
watchvar = str("1-973-339-7436") #Phone number to look for

rownum = 0
colnum = 0
header = "No Header"
X = float(0) # MINUTES
Y = str("NO DF")# DIAL FROM
Z = str("NO DT")# DIAL TO

watchcol = -1
verbose = str("N")
spacenum = int(0)
tminutes = float(0)

if os.path.isfile(outfile):  #removes the old file if it exists
        os.remove(outfile)

#watchvar = input("Enter variable to watch - X, Y, or Z: ").upper()
#tolerance = float(input("Enter Tolerance: "))
verbose = input("Verbose? - Y or N: ").upper()
watchvar = input(str("Enter # to look for in this format [1-973-339-7436]: ")) #Phone number to look for
outfile=watchvar+outfile #attaches extension number to file name start

watchcolx = 3
watchcoly = 4
watchcolz = 5

       # print("Only X, Y or Z values are allowed. Program terminated.")
       # sys.exit("only X, Y or Z values allowed")

csvfile = open(infile)

dialect = csv.Sniffer().sniff(csvfile.read(1024))
csvfile.seek(0)

print(" ") 
#print("The Delimiter is [", dialect.delimiter, "]") #can't get this to work
print("Analyzing Extension[", watchvar, "]")
print(" ") 

reader = csv.reader(csvfile, dialect)
# ... process CSV file contents here ...
reader = csv.reader(open(infile), delimiter=dialect.delimiter, quoting=csv.QUOTE_NONE)

csvfile2 = open(outfile, 'a', newline='') #this opens the file
with csvfile2 as csvfile2:


        
 for row in reader:
    if rownum == 0:
      header = row
      #print(header)
      xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
      xyzspacer.writerow(["MINUTES   FROM   TO"]) #writes a faux header
      
    colnum = 0
    
    for col in row:
     if rownum > 0:
            #print("Column Number:", colnum, "Row Number:", rownum)
            #print(header[colnum], col)
            if colnum==watchcolx:
                X=float(col)
            if colnum==watchcoly:
                Y=str(col)
            if colnum==watchcolz:
                Z=str(col)
     colnum += 1
     if Y == watchvar:            
        if verbose == 'Y':
           print("---------- From Number Detected ----------")
        xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        xyzspacer.writerow([X, Y, Z]) #writes to file xyz locations
        spacenum += 1
        tminutes = tminutes+X
     if Z == watchvar: 
     #if lastZ != Z and watchcol == 2: #Z variable and Colum 2
        if verbose == 'Y':    
           print("---------- To Number Detected ----------")
        xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        xyzspacer.writerow([X, Y, Z]) #writes to file xyz locations
        spacenum += 1
        tminutes = tminutes+X
     #if verbose == 'Y':        
       #print("XYZ FROM VARIABLES: ", X, Y, Z) #writes to terminal
     #xyzspacer = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
     #xyzspacer.writerow([X, Y, Z]) #writes to file xyz locations

    
    rownum += 1
print("Analyzed ", rownum, "calls.")
print("Added", spacenum, "instances to ", outfile)
print(" ")
print("Calls: ", spacenum)
print("Minutes: ", tminutes)




