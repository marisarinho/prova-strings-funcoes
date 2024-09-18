def cripto(str):
    cripto=''
    for i in a:
        if i=='A' or i=='a':
            cripto+='@'
        elif i=='E' or i=='e':
            cripto+='3'
        elif i=='I' or i=='i':
            cripto+='!'
        else:
            cripto+=i
        
    return cripto
a=input('frase: ')
print(f'{cripto(a)}')
