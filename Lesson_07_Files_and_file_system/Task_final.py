import os
import shutil
from pathlib import Path

for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f: # создаем файлы 0..10
        f.write('Hello, world!') # записываем в них фразу
os.mkdir('new_dir') # создаем директорию 'new_dir'
for i in range (2, 10, 2): # цикл перебирает четные имена файлов
    f = Path(f'file_{i}.txt')
    f.replace('new_dir' / f) # и перемещает эти файлы в директорию
shutil.copytree('new_dir', Path.cwd() / 'dir_new') # копируем всю инфу из 'new_dir' в 'dir_new'

# таким образом, в корневой директории будут файлы 1, 3, 5, 7
# в 'new_dir' и 'dir_new' - файлы с четными номерами