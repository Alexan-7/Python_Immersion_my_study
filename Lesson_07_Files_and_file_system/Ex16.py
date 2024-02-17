# получение текущего пути
import os
from pathlib import Path # с большой буквы - значит КЛАСС

print(os.getcwd())
print(Path.cwd()) # Current Work Dir - текущая рабочая директория