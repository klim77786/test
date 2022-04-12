"""Данные об email-адресах студентов хранятся в словаре:
Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и
в формате имя_пользователя@домен."""

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

for key, value in emails.items():
    value = ','.join(value)
    my_line = value.replace(',', '@' + key + ' ') + '@' + key
    my_list = my_line.split()
    print('Почтовые адреса в алфавитном порядке:', *sorted(my_list), sep='\n')
    print()

sp = []
for key, value in emails.items():
    for i in range(len(value)):
        sp.append(value[i] + '@' + key)
print(*sorted(sp), sep='\n')
