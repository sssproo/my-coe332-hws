import names


def calculate(name_list):
    for name in name_list:
        print(name, len(name) - 1)


def main():
    name_list = []
    cnt = 0
    while cnt < 5:
        name = names.get_full_name()
        if name not in name_list:
            name_list.append(name)
            cnt += 1
    calculate(name_list)


if __name__ == '__main__':
    main()

