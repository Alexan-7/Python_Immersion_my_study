color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'Оранжевый': # палочка - это "ИЛИ" 
        print('Любитель яркого')
    case 'зеленый':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _: # равноценно записи ELSE
        print('Тебя не понять')