


n = int(input('Ingrese un numero entre 1 y 12: '))

if n >0 and n<13:
    for x in range(1,13):
        print(f'{n} X {x}: {n*x}')
else:
        print(f'Numero fuera de rango\n{n} no esta entre 1 y 12')
