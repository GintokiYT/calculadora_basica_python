# Importaciones
import os, sys
os.system('cls')

# Valores para operar
numeros = [0,0]
# Opcion si sera suma, resta, multiplicación y division
opcion = "0"

print('\tCALCULADORA BASICA')

# Obtenemos la opcion del usuario
while(opcion == "0") :
    opcion = input('Ingrese la opcion que desea realizar.' + 
             '\nSuma[1]\nResta[2]\nMultiplicacion[3]\nDivision[4]\nSalir[5]\nOpcion: ')

    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" :
        break
    elif opcion == "5" :
        os.system('cls')
        print('Gracias por su preferencia')
        input('\nPress a key to continue')
        sys.exit()    
    else :
        os.system('cls')
        print('\tCALCULADORA BASICA')
        print('Opcion no valida intente nuevamente!')
        opcion = "0"

# Obtener Valores
def obtenerValor(texto, position) :
    operacion = ""
    if opcion == "1" : operacion = 'Suma'
    if opcion == "2" : operacion = 'Resta'
    if opcion == "3" : operacion = 'Multiplicacion'
    if opcion == "4" : operacion = 'Division'

    try :
        os.system('cls')
        print('\tCALCULADORA BASICA')
        print(f'Operación {operacion}')
        numero = float(input(f'Ingrese el {texto} valor : '))
        numeros[position] = numero
    except :
        obtenerValor(texto, position)

# Validar si es entero o decimal
def sincero(resultado) :
    retorno = resultado

    if resultado % 1 == 0 :
        retorno = int(resultado)
    
    return retorno

# Validamos que operacion realizara
if opcion == "1" :
    os.system('cls')
    print('\tCALCULADORA BASICA')

    obtenerValor('primer', 0)
    obtenerValor('segundo', 1)

    resultado = numeros[0] + numeros[1]
    print(f'La suma es : {sincero(resultado)}')

elif opcion == "2" :
    os.system('cls')
    print('\tCALCULADORA BASICA')

    obtenerValor('primer', 0)
    obtenerValor('segundo', 1)

    resultado = numeros[0] - numeros[1]
    print(f'La resta es : {sincero(resultado)}')

elif opcion == "3" :
    os.system('cls')
    print('\tCALCULADORA BASICA')

    obtenerValor('primer', 0)
    obtenerValor('segundo', 1)

    resultado = numeros[0] * numeros[1]
    print(f'La multiplicacion es : {sincero(resultado)}')

elif opcion == "4" :
    os.system('cls')
    print('\tCALCULADORA BASICA')

    obtenerValor('primer', 0)
    obtenerValor('segundo', 1)

    resultado = numeros[0] / numeros[1]
    print(f'La division es : {sincero(resultado)}')
