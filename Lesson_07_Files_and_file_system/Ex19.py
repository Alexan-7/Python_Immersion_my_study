# создание директории с несколькими уровнями вложенности
import os
from pathlib import Path

# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_os_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_os_dir').mkdir(parents=True)

# доп. параметр - создать саму дир-ю и все родительские дир-и