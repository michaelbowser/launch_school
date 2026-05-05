info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
removed = info.split(':')
new = '+'.join(removed)
print(new)
