# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.

# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) 
# считать двумя словами.
# Цифры за слова не считаем.

# Отсортируйте по убыванию значения количества повторяющихся слов.

def ten_popular(text: str):
    import re
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    words = re.split(" |'", text.lower())
    temp_list = []
    for el in words:
        if not (el in temp_list) and not el.isdigit():
            temp_list.append(el)
    temp_list2 = []
    for el in temp_list:
        a = el, words.count(el)
        temp_list2.append(a)

    return sorted(temp_list2, key=lambda sort_col: sort_col[1], reverse=True)[:10]


text = "Hello world. Hello Py it's thon. Hello again."
print(ten_popular(text))
