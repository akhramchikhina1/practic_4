counter=str(input('Введите счёт команд: '))
counter=counter.split(':')
count_first=int(counter[0])
count_second=int(counter[1])
if count_first>count_second:
    print(count_first)
elif count_first<count_second:
    print(count_second)
else:
    print('0')