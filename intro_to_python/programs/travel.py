destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False
    
print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
