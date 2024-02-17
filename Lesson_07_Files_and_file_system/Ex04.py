f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'Мир!'.encode('cp1251')) # разные кодировки!
f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()