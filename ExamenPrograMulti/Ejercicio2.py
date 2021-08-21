from Clear import clear


file = open("base.txt",'w')
file.close()

def IngresarDatos():
    file = open('base.txt','a')
    codigo = input('Ingrese su codigo(Identidad):')
    nombre = input('Ingrese su nombre:')
    direccion = input('Ingrese su direccion:')
    puesto = input('Ingrese su puesto:')
    salario = input('Ingrese su salario:')
    empleado = f'{codigo},{nombre},{direccion},{puesto},{salario}\n'
    file.write(empleado)
    clear()


def MostrarDatos():
    file = open('base.txt','r')
    text = file.read()
    if  text != '':
        empleados = text.split('\n')
        n = 1
        print('\n*******Empleados*********')
        for x in empleados:
            if(x != ''):
                print(f'\nEmpleado #{n}\n')
                codigo,nombre,direccion,puesto,salario= x.split(',')
                print(f'Codigo: {codigo}\nNombre: {nombre}\nDireccion: {direccion}\nPuesto: {puesto}\nSalario: {salario}')
                n += 1
    else:
        print('No hay empleados')


menu = '''
**********Menu************
1.Ingresar empleado 
2.Ver empleados 
3.Salir 
opcion: '''

while True:
    opcion = input(menu)
    if opcion == '1':
        IngresarDatos()

    if opcion == '2':
        MostrarDatos()
    
    if opcion == '3':
        file.close()
        break
