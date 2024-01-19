data = ['http:', '', 'www.fa.ru', 'org', 'dep', 'is', 'Pages', 'Home.aspx']
url = '/☺'.join(data)
print(url)

text = 'ОднАЖды В СТудёнУЮ зимНЮю пОрУ ехАЛ ГреКА чеРЕз РеКу'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

text2 = 'Однажды в студёную зимнюю пору ехал грека через реку'
print(text2.startswith('Однажды'))
print(text2.endswith('через', 0, -5)) # от начала - исключить последние 5 символов
print(f'{text2 = :>80}')