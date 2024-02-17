text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')