# Multiplication Table Printer , But Skip the fifth iteration

for i in range(1,11):
    if i == 5:
        continue # skip 5th iteration
    else:
        print("5 * ",i,"=",i*5)
        