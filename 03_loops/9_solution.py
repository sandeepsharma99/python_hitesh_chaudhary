# List Uniqueness Checker : Check all element in list are unique. if dublicate is found, exit the loop and print the dublicate

items = ["apple","banana","apple","Orange","Mango"] 

unique_items = set()

for  item in items:
    if item in unique_items:
        print("Dublicate :",item)
        break
    unique_items.add(item)