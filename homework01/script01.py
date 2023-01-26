words = []
with open('/usr/share/dict/words','r') as f:
    contents = f.readlines()
    for i in range(len(contents)):
        words.append(contents[i].strip('\n'))
words.sort(key=lambda x: (len(x), x), reverse=True)
print(words)
