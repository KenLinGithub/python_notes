name_list = []
while True:
    name = input('Please input a guest name: ')

    if name == '':
        break

    name_list.append(name)

name_list = list(set(name_list))

print(len(name_list))

if len(name_list) % 12 == 0:
    print(len(name_list) // 12)

print((len(name_list) // 12) + 1)