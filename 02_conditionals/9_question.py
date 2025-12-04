# Check leap Year:
Year = 2028  
if (Year % 400 == 0) or (Year %4 == 0 and Year %100 !=0):
    print(Year, " :This is leap Year")
else:
    print("This is Not a leap Year")