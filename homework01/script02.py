import names

cnt = 0
while cnt < 5:
    name = names.get_full_name()
    if len(name) == 9:
        print(name)
        cnt += 1

