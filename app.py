#Создаем словари
account1 = {'login' : 'ivan', 'password' : 'q1'}
account2 = {'login' : 'petr', 'password' : 'q2'}
account3 = {'login' : 'olga', 'password' : 'q3'}
account4 = {'login' : 'anna', 'password' : 'q4'}

user1 = {'name' : 'Иван', 'age' : '20' , 'account' : account1}
user2 = {'name' : 'Петр', 'age' : '25' , 'account' : account2}
user3 = {'name' : 'Ольга', 'age' : '18' , 'account' : account3}
user4 = {'name' : 'Анна' , 'age' : '27' , 'account' : account4}

#Создаем список из словарей
user_list = [user1, user2, user3, user4]


key_name = input('Введите ключ (name или account): ')
#Проверяем ключ
if key_name.lower() == 'name' or key_name.lower() == 'account':
    for i in range(len(user_list)):
        print(f'Значение ключа {key_name.lower()} для юзера {i+1} = {user_list[i]["name"]}')
else:
    print('Введенный ключ не найден!')

#Проверяем число и выводим данные
try:
    number_user = int(input('Введите порядковый номер: '))
    print(f'\nДанные по юзеру № {number_user}')
    user = number_user - 1
    print(f'имя: {user_list[user]["name"]}')
    print(f'возраст: {user_list[user]["age"]}')
    print(f'логин: {user_list[user]["account"]["login"]}')
    print(f'пароль: {user_list[user]["account"]["password"]}')
#Создаем переменную через цикл находим сумму возраста и находим средний
#возраст всех юзеров
    average_age = 0
    for i in range(len(user_list)):
        average_age += int(user_list[i]["age"])
    average_age = average_age / int(len(user_list))
    print(f'Средний возраст пользователей: {average_age}')
#Перенос в конец списка
    moving_user = int(input('\nВведите номер пользователя, который нужно переместить в конец: '))
    print(f'Список до изменения:\n {user_list}')
    element = user_list.pop(moving_user - 1)
    user_list.append(element)
    print(f'Список после изменения:\n {user_list}')
except:
    print('Пользователь с указанным номером не найден')
  

