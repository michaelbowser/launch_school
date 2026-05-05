def all_caps(word):
    if len(word) > 10:
        print(word.upper())
    else:
        print(word)

word = input('Please input a word  ')
all_caps(word)
