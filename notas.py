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
print(lista)
