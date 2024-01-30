toys = {'машинка', 'мишка', 'кукла', 'вертолет'}

kindergarten_1 = {'машинка', 'кукла'}
kindergarten_2 = {'машинка', 'вертолет'}
kindergarten_3 = {'машинка', 'кукла', 'вертолет'}
kindergarten = kindergarten_1 | kindergarten_2 | kindergarten_3

for i in toys:
    if i != kindergarten:
        noy = i

vse = kindergarten_1&kindergarten_2&kindergarten_3

print(f'игрушки которых нет в детских садах{noy}\nигрушки которыен есть во всех детских садах{vse}')

