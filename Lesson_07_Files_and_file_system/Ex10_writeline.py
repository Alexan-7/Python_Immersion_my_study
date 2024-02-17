text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit,',
        ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ',
        'ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))