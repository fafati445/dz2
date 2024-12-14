def openfiles():
    texts = ['1.txt', '2.txt', '3.txt']
    list_t = []
    for text in texts:
        with open(text, encoding='utf-8') as t:
            x = t.readlines()
            list_t.append([text,'\n', str(len(x)),'\n', ''.join(x),'\n\n'])
    list_t = sorted(list_t, key=lambda x: x[2])
    with open('4.txt', 'w', encoding='utf-8') as a:
        a.write(''.join(list_t[0]))
        a.write(''.join(list_t[1]))
        a.write(''.join(list_t[2]))

openfiles()
