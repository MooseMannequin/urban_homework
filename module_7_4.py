team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 9
score2 = 11
team1_time = 13
team2_time = 18
tasks_total = score1 + score2
time_avg = round(tasks_total / (team2_time+team1_time), 2)

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде %s участников: %s' % (team1, team1_num))
print('В команде %s участников: %s' % (team2, team2_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print('Команда {} решила задач: {}'.format(team2, score2))
print('{} решили задачи за {} мин'.format(team2, team2_time))

print(f'Команды решили {score1} и {score2} задач!')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} мин на задачу')
