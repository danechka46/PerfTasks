import json

dict = {}
with open("values.json") as read_file:
    data_value = json.load(read_file)
with open("tests.json") as read_file:
    data_tests = json.load(read_file)

tests = (data_tests['tests'])
values = (data_value['values'])

for item in values:  #Заполняем пустой словарь полями id и value
    dict[item['id']] = item['value']

def func(q): #Функция для заполнения пустых полей value по совпадению c id
    for item in range(len(q)):
        if q[item].get('value') is not None:
            q[item]['value'] = dict[q[item]['id']]
        if q[item].get('values') is not None:
            func(q[item]['values'])


func(tests)

with open("report.json", "w") as file:
    json.dump(tests, file, indent=2)