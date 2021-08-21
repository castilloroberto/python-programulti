import os
def clear(): os.system('cls') #on Windows System



persons = []


n = int(input("Numero de personas a ingresar:"))

while(len(persons) < n):
    clear()
    print(f"Persona #{len(persons) +1}")
    id = input("Identidad:")
    name = input("Nombre:")
    age = int(input("Edad:"))
    heigh = float(input("Estatura:"))
    campus = input("campus:")
    dic = {'id':id,'Nombre':name,'Edad':age,'Estatura':heigh,'Campus':campus}
    persons.append(dic)

clear()
print("Personas ingresadas:")
for person in persons:
    print(f"\nid: {person['id']}, Estatura: {person['Estatura']}")