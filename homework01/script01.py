words = []
with open('words.txt', encoding='utf-8') as file:
    contents = file.readlines()
    for i in range(len(contents)):
        words.append(contents[i].strip('\n'))
words.sort(key=lambda x: (len(x), x), reverse=True)
print(words)
