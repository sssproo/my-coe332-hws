words = []
with open('words','r') as f:
    contents = f.readlines()
    for i in range(len(contents)):
        words.append(contents[i].strip('\n'))
words.sort(key=lambda x: (len(x), x), reverse=True)
for i in range(5):
  print(words[:5])
