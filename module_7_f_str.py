team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

formatted_string_1 = "В команде Мастера кода участников: %d !" % team1_num
formatted_string_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

formatted_string_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
formatted_string_4 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)

formatted_string_5 = f"Команды решили {score_1} и {score_2} задач."
formatted_string_6 = f"Результат битвы: {challenge_result}"
formatted_string_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"

print(formatted_string_1)
print(formatted_string_2)
print(formatted_string_3)
print(formatted_string_4)
print(formatted_string_5)
print(formatted_string_6)
print(formatted_string_7)