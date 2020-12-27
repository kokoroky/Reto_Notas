def set_alumnos():
    print("--------------------------------------------------------------------------------")
    print("Registro de los Alumnos")
    lista_alumnos = []
    while True:
        alumno = set_registro_alumno()
        lista_alumnos.append(alumno)
        print("--------------------------------------------------------------------------------")
        print("¿Desea Registrar un Nuevo Alumno?")
        print("1: Sí")
        print("2: No")
        try:
            option = input(f"Ingrese el número de la opción que desea: ")
            if (option=="1"):
                print("Opción escogida: Sí")
            elif (option=="2"):
                break
            else:
                print("Debe escoger una opción de la lista.")
        except KeyboardInterrupt:
            print('\n')
            print("Proceso terminado.")
            sys.exit()
        except Exception as e:
            print(e.__class__.__name__)
            print(f'Ocurrio un problema : {str(e)}')

    print("--------------------------------------------------------------------------------")
    print("Los Alumnos Registrados fueron")
    print(lista_alumnos)

def set_registro_alumno():
    print("--------------------------------------------------------------------------------")
    print("Registro del Alumno") 
    nombre_alumno = set_nombre_alumno()
    numero_notas = set_numero_notas()
    lista_notas = set_notas(numero_notas)
    alumno = dict(nombre_alumno = nombre_alumno, numero_notas = numero_notas, lista_notas = lista_notas)
    print("--------------------------------------------------------------------------------")
    print(f'Alumno en diccionario : {alumno}')
    return alumno


def set_nombre_alumno():
    print("--------------------------------------------------------------------------------")
    print("Datos del Alumno")
    try:
        nombre = input(f"Ingrese el Nombre del Alumno: ")
        print("El nombre Ingresado fue " + nombre)
        return nombre
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except Exception as e:
        print(e.__class__.__name__)
        print(f'Ocurrio un problema : {str(e)}')


def set_numero_notas():
    print("--------------------------------------------------------------------------------")
    print("Numero de Notas del Alumno")
    try:
        num_notas = input(f"Ingrese la Cantidad de Notas del Alumno: ")
        int(num_notas)
        print("Cantidad de Notas ingresada: " + num_notas)
        return num_notas
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except ValueError:
        print("Ingrese un valor correcto.")
        return set_numero_notas()
    except Exception as e:
        print(e.__class__.__name__)
        print(f'Ocurrio un problema : {str(e)}')

def set_notas(nro_notas):
    print("--------------------------------------------------------------------------------")
    print("Notas del Alumno")
    lista = []
    nro_vueltas = 0
    while nro_vueltas < int(nro_notas):
        nro_vueltas += 1
        try:
            nota = int(input(f"Ingrese nota {nro_vueltas} :"))
            lista.append(nota)
        except ValueError as e:
            print(f'Ocurrio un problema, solo debes ingresar números')
            nro_vueltas -= 1
        except KeyboardInterrupt:
            print('\n')
            print("Proceso terminado.")
            sys.exit()
        except Exception as e:
            print(e.__class__.__name__)
            print(f'Ocurrio un problema : {str(e)}')
            break
    print("--------------------------------------------------------------------------------")
    print(f"Las {nro_notas} registradas fueron : {lista}")
    print(f"El Promedio es  : {promediar_notas(lista)}")
    lista.sort()
    print(f"La menor nota  es  : {lista[0]}")
    print(f"La mayor nota  es  : {lista[len(lista) - 1]} \n")
    return lista


def promediar_notas(lista):
    laSuma = 0
    for i in lista:
        laSuma = laSuma + i
    return (laSuma)/len(lista)


set_alumnos()

#numero_notas = set_numero_notas()
#set_notas(numero_notas)