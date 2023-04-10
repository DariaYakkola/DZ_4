shadoof = int(input('Введите число журавликов: '))
if shadoof % 6 > 0:
    print('Нельзя определить! ')
else:
    petya_serezha = (shadoof / 2) / 3
    kate = (petya_serezha + petya_serezha) * 2
    print(f'Петя и Сережа сделали по {int(petya_serezha)} журавлика,'
          f' а Катя {int (kate)} журавликов')
