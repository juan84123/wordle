letras_verificadas = [] #se guardan las letras verificadas
cantidad_letras = 5 #cantidad de letras que tiene la plabra 
palabra_secreta = "calle" # palabra secreta 
intentos = 0 #se pone en 0 la cantidad de intentos
aux=[] #un auxiliar para guardar la palabra secreta formateada

def convertir_secreto(): #se usa esta funcion para cambiar el formato de la palabra secreta, de manera hacer la comparacion final
    for i in range(cantidad_letras):
        aux.append(f"[{palabra_secreta[i]}]")

convertir_secreto() 

def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] #True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta #busca si la letra esta en la palabra secreta
        if las_palabras_son_iguales: #significa que la palabra ingresada es igual a la palabra secreta 
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra: #si la letra esta en la palabra
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            letras_verificadas.append(palabra_ingresada[i])#si no esta en la palabra
    return letras_verificadas


while intentos < 6: #se encarga de que el juego termine despues de la cantidad de oportunidades definidas
    print(f"te quedan {6 - intentos} intentos")
    intentos = intentos + 1 #cada intento disminuye 1 
    palabra_ingresada = input("Ingrese una palabra: ")
    print(f"la palabra ingresada es: {palabra_ingresada}")
    print(verificador_palabra(palabra_ingresada, palabra_secreta)) #llama a la funcion que hace la corroboracion de letras en la palabra secreta
    letra_veri_final_juego = verificador_palabra(palabra_ingresada, palabra_secreta) # guarda la palabra para compararlo con la palabra secreta
    if letra_veri_final_juego == aux: #hace la comparacion y si se True, termina el juego
        print(f"Felicidades encontraste la palabra: {palabra_secreta}")
        break