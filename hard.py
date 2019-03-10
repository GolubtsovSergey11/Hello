print('Медицинская анкета')
name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
age = int(input('Сколько Вам лет: '))
weight = int(input('Введите свой вес: '))
print('Фамилия:', surname, 'Имя:', name, 'Вам', age, 'лет', 'Ваш вес:', weight)

if age < 30 and 50 <= weight <= 120:
    print(name, surname, age, 'лет,',  weight, 'вес,', '- хорошее состояние.')
elif 30 <= age <= 40 and 50 > weight <120:
    print(name, surname, age, 'лет,',  weight, 'вес,', '- следует заняться собой.')
elif age > 40 and 50 > weight <120:
    print(name, surname, age, 'лет,',  weight, 'вес,', '- следует обратится к врачу.')
else:
    pass

