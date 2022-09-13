# Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
# - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.

def txt_calculator(path):
    result = None
    operation = []
    with open(path, 'r') as text_file:
        while True:
            if len(operation) == 3:
                try:
                    if operation[1] == "+":
                        result = operation[0] + operation[2]
                    elif operation[1] == "-":
                        result = operation[0] - operation[2]
                    elif operation[1] == "*":
                        result = operation[0] * operation[2]
                    else:
                        result = operation[0] / operation[2]

                except:
                    print("ERROR: Incorrect txt format!")
                    return None
            
                operation.clear()
                operation.append(result)        

            line = text_file.readline()
            if line:
                try:
                    operation.append(float(line))
                except ValueError:
                    operation.append(line.rstrip())
            
            else:
                break

    return result

print(txt_calculator("Challenge21.txt"))
    