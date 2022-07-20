#3 Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби

users_list = []
hobby_list = []
user_hobby_dict = {}


with open('users.csv', 'r', encoding='utf-8') as users:
    for line in users:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        user = ','.join(line)
        users_list.append(user)


with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
    for line in hobbies:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        hobby_list.append(line)


for number in range(len(users_list)):
    if number < len(hobby_list):
        user_hobby_dict[users_list[number]] = hobby_list[number]
    else:
        user_hobby_dict[users_list[number]] = None
print(user_hobby_dict)


with open('users_hobby.txt', 'w+', encoding='utf-8') as users_hobby:
    for key, value in user_hobby_dict.items():
        users_hobby.write(f'{key}, {value}\n')