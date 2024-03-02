name=input('Здравствуйте! Как Вас зовут? ')
print(f'Очень приятно, {name}! Меня зовут Марк.')
years=int(input('Сколько Вам лет? '))
if years>78:
    print(f'Да, {name}, Вы старше меня на {years-78} лет')
else:
    print(f'Да, {name}, я старше Вас на {78-years} лет')