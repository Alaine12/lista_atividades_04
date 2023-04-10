"""Faça um programa para imprimir:
1
1   2
1   2   3
.....
1   2   3   ...  n
   para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""
def imprimir(valor):
    if isinstance(valor, int):
        x = 1
        while x <= valor:
            y = 1
            texto = ''
            while y <= x:                
                texto += str(y) + "\t"
                y += 1
            print 
            texto
            x += 1
            num_cascate2(9)
1
12
123
1234
12345
123456
1234567
12345678
123456789