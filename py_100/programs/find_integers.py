def find_integers(things):
    return [element
            for element in things
            if type(element) is int]
 #   result = []
  #  for element in things:
   #     if type(element) is int:
    #        result.append(element)
    #return result 

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
           -4, None, {1, 3, 4}, False)
integers = find_integers(my_tuple)
print(integers)


