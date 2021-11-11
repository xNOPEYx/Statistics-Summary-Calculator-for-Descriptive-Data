# COURSE: CMPS 3500
# CLASS Project
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# DATE: 11/01/2021
# STUDENT 1: Dominic Fanucchi
# STUDENT 2: Ronaldo Mojica
# STUDENT 3: 
# DESCRIPTION: IMPLEMENTATION OF A STATISTICS SUMMARY CALCULATOR

# file imports
#import dfanucchi as df

# importing csv module
import csv

def print_menu():
    print 30 * "-", "M A I N  M E N U", 30 * "-"
    print "1.       Count"
    print "2.       Unique"
    print "3.       Mean"
    print "4.       Median"
    print "5.       Mode"
    print "6.       Standard Deviation (SD)"
    print "7.       Variance"
    print "8.       Minimum"
    print "9.       20 Percentile (P20)"
    print "10.      40 Percentile (P40)"
    print "11.      50 Percentile (P50)"
    print "12.      60 Percentile (P60)"
    print "13.      80 Percentile (P80)"
    print "14.      Maximum"
    print "15.      End Program"
    print 78 * "-"

# naming csv files
rideshare = "Boston_Lyft_Uber_Data.csv"
sample = "InputDataSample.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv files
with open(sample, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

	# get total number of rows
	print("Total number of rows: %d"%(csvreader.line_num))

# printing the field names
#print('Field names are: ' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
#for row in rows[:5]:
	# parsing each column of a row
#	for col in row:
#		print("%10s"%col),
#	print('\n')

loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-15]: ")
    if choice == 1:
        print "Menu 1 has been selected!\n"
    elif choice == 2:
        print "Menu 2 has been selected!\n"
    elif choice == 3:
        print "Menu 3 has been selected!\n"
    elif choice == 4:
        print "Menu 4 has been selected!\n"
    elif choice == 5:
        print "Menu 5 has been selected!\n"
    elif choice == 6:
        print "Menu 6 has been selected!\n"
    elif choice == 7:
        print "Menu 7 has been selected!\n"
    elif choice == 8:
        print "Menu 8 has been selected!\n"
    elif choice == 9:
        print "Menu 9 has been selected!\n"
    elif choice == 10:
        print "Menu 10 has been selected!\n"
    elif choice == 11:
        print "Menu 11 has been selected!\n"
    elif choice == 12:
        print "Menu 12 has been selected!\n"
    elif choice == 13:
        print "Menu 13 has been selected!\n"
    elif choice == 14:
        print "Menu 14 has been selected!\n"
    elif choice == 15:
<<<<<<< HEAD
        print "Menu 15 has been selected!"
        print "!PROGRAM TERMINATED!\n"
#Terminate code completely 
#Add M key that allows user to go back to menuy options.
#Add code that takes user back to Menu
=======
        print "Quit option selected!\n"
>>>>>>> 69a40527fb9b09d4e70eecf09e10cff04b560373
    else:
        raw_input("Wrong option selection. Enter any key to try again...")
        
