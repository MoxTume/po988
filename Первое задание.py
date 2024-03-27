import csv  # Подгружаем библиотеку csv для работы с файлами .csv
with open('students.csv', encoding='utf8') as file:  # открываем файл students.csv
    reader = list(csv.reader(file, delimiter=','))[1:]
    count_class = {}
    sum_class = {}
    for idd, name, titleProject_id, level, score in reader:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {idd}")
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)
    for el in reader:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)
with open('students_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file, delimiter=',')
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writerows(reader)
