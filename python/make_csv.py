students = {
    'asdf': {
        '순번': '01',
        '이름': '김성훈'
    },
    'asdf2': {
        '순번': '02',
        '이름': '김은정'
    }
}

students2 = {
    {
        '순번': '02',
        '이름': '김은정'
    },
    {
        '순번': '03',
        '이름': '김인성'
    }
}

# with open('a.csv', 'w', encoding='utf-8') as f:
#     f.write('number, name\n')
#     for number, name in students.items():
#         f.write(f'{number}, {name}\n')
import csv
with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    print(type(students))
    for item in students.values():
        csv_writer.writerow(item)