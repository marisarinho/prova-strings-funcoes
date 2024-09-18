data=input('ano ').split('/')
nome=input('nome ')
a=nome.split()
b=a[0].capitalize()+a[-1].capitalize()
# dia, mes, ano=input(.split())
dia=data[-3]
mes=data[-2]
ano=data[-1]
print(f'{ano}{mes}{dia}_{b}')
