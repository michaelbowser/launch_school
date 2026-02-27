forenames =['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']


index = 0
while index < len(forenames):
    if index >= len(surnames):
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1
