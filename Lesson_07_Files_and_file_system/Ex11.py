text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim?',
        'Ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip!', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.