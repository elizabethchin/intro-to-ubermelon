log_file = open("um-server-01.txt")
#creates a file object from text file 

#defines a function called sales reports
def sales_reports(log_file):
"""Prints sales information for Monday."""

    #get each line in log_file
    for line in log_file:
        #loops through each line
        line = line.rstrip()
        #removes white space
        day = line[0:3]
        #keeps first three indicies of day
        if day == "Mon":
            #if day equals to value it will print it
            print(line)


sales_reports(log_file)
#calls the function
