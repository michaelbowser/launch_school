my_list = [6, 3, 0, 11, 20, 17]
"""
# Even function
index = 0
while index < len(my_list):
    number = my_list[index]
    if number % 2 == 0:
        print(number)

    index += 1
"""    
for number in my_list:
    if number % 2 != 0:
        print(number)
