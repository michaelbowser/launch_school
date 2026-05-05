def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))


def add_item(item, lst=[]):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))


def add_item(item, lst=[1,2,3]):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
