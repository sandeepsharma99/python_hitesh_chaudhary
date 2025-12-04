# Find the first Non-Repeated Character

input_str = "teeterjhsgdfshdf"
for char in input_str:
    if input_str.count(char) == 1:
        print(char,"is non-repeated-character")
        break # exits the loop immediately
