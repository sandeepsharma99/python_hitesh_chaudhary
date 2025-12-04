# Coffee Customization : Customize a coffe order :"Small", "Medium", "Large" with an option for "Extra Short" of espresso.
extra_shot = True
order_size = "Large"
if extra_shot:
    coffee = order_size + "coffe withn an extra shot"
    print()
    if order_size == "Small":
        print("Small order")
    elif order_size == "Medium":
        print("Medium")
    elif order_size == "Large":
        print("Large")
    else:
        print("Invalid input")
    