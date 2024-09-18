def contador(m,n):
    a=0
    for linha in range(LINHA):
        cont=m[linha].count(n)
        a+=cont
    return a
n=int(input('numero a ser buscado: '))    
LINHA=int(input('linhas '))
COLUNA=int(input('colunas '))
m=[[None]*COLUNA for i in range(LINHA)]
for linha in range(LINHA):
    for coluna in range(COLUNA):
        m[linha][coluna]=int(input('num matriz '))
print(f'{contador(m,n)}')
