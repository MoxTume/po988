import csv  # Подгружаем библиотеку csv для работы с файлами .csv
with open('students.csv', encoding='utf8') as file:  # открываем файл students.csv
    reader = list(csv.DictReader(file, delimiter=','))[1:]
    data = sorted(reader, key=lambda x: x['titleProject_id'])
input_id = input('Введите id проекта')
while input_id != 'СТОП':
    input_id = int(input_id)
    for el in data:
        if int(el['titleProject_id']) == input_id:
            surname, name, p = el["Name"].split(' ')
            print(f"Проект № {input_id} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el['score']}.")
            break
    else:
        print('Ничего не найдено')
    input_id = input('Введите id проекта')
