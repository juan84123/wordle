letras_verificadas = [] #se guardan las letras verificadas
cantidad_letras = 5 #cantidad de letras que tiene la plabra 
palabra_secreta = "calle" # palabra secreta 

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