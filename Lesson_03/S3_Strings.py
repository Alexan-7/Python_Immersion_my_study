text = 'Hello, World!'
print(text[6])
print(text[3:7]) # срез с 3й буквы включ-но по 7ю искл-но
print(text.count(('l')))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

new_txt = text.replace('l', 'L', 2) # 3й элемент - кол-во замен
print(text, new_txt, sep='\n')

text2 = 'Hello, World!'
print(text2[::-1])