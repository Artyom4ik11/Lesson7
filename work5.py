import os
import json

ROOT_DIR = r'C:\Users\пк\PycharmProjects\pythonProject\venv\Lesson7\work5.py'

size_cont_dict = {}

for el in os.scandir(ROOT_DIR):
    size = el.stat().st_size
    len_size = len(str(size))
    key_dict = int('1'+'0'*len_size)

    if key_dict not in size_cont_dict:
        size_cont_dict[key_dict] = [0, []]

    size_cont_dict[key_dict][0] += 1

    el_type = el.name.split('.')[1]
    if el_type not in size_cont_dict[key_dict][1]:
        size_cont_dict[key_dict][1].append(el_type)

size_cont_dict = {x: (size_cont_dict[x][0], size_cont_dict[x][1]) for x in size_cont_dict}
print(size_cont_dict)

with open(os.path.join(os.path.dirname(__file__), f'{os.path.basename(ROOT_DIR)}_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(size_cont_dict, f, indent=4)
    print('Файл успешно сохранен') # много раз пытался сделать. выдаёт что нет такого файла хоть он и есть!