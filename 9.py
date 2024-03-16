poroda=input('Собака короткошерстной породы? ')
if poroda=='да':
    high=input('Рост собаки менее 50 см? ')
    if high == 'да':
        tail=input('У собаки короткий хвост? ')
        if tail == 'да':
            print('английский бульдог')
        else:
            ears=input('У собаки длинные уши?')
            if ears== 'да':
                print('гончая')
            else:
                body=('У собаки короткое тело? ')
                if body=='да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        weight=input('Собака весит более 50 кг?' )
        if weight=='да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    high = input('Рост собаки менее 50 см? ')
    if high == 'да':
        character = input('У собаки доброжелательный характер? ')
        if character == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        high_second=input('У собаки менее 70 см? ')
        if high_second=='да':
            ears = input('У собаки длинные уши?')
            if ears == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            color=input('Окрас рыжий с белыми отметинами? ')
            if color=='да':
                print('сенбернар')
            else:
                while_color=input('Белоснежный окрас? ')
                if while_color == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
