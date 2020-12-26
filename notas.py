nota=0
lista = []
nro_vueltas = 0

while nro_vueltas < 5:
    nro_vueltas += 1
    try:
        nota = int(input(f"Ingrese nota {nro_vueltas} :"))
        lista.append(nota)
    except ValueError as e:
        print(f'Ocurrio un problema, solo debes ingresar números')
        nro_vueltas -= 1
    except Exception as e:
        print(e.__class__.__name__)
        print(f'Ocurrio un problema : {str(e)}')
def sumalista(lista):
    nota=0
    promedio=0
    laSuma = 0
    for i in lista:
        laSuma = laSuma + i
    return laSuma

promedio=sumalista(lista)/5

 
#Vamos a poner los números en una lista
#numeros = []

# Asumir que el mayor es el primero de la lista
mayor = lista[0]
menor = lista[0]

# Recorrer y comparar
for numero in lista:
    if numero > mayor:
        mayor = numero
    else:
        if numero < menor:
            menor = numero  

#Promedio de notas
print("El promedio es:", promedio)
# Imprimir el resultado
print("Mayor:", mayor)

# Imprimir el resultado
print("Menor:", menor)
