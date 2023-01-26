word = []
sorted_words =[]

with open('words','r') as f:

    words =f.read().splitlines()

sorted_words =words.sort(key=len,reverse=True)

print(words[:5])
