import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..') # changedirectory
print(os.getcwd())
print(Path.cwd())