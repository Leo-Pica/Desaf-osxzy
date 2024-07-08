#ordenamos los libros por sus códigos de mayor a menor
codigos=[123,456,789,234,567,787] #lista con codigos
libros_ordenados=sorted(codigos,reverse=True)
#sorted es para crear la lista, reverse invierte
#el orden y le da el valor de True (verdadero)
print("Lista de códigos decreciente: ", libros_ordenados)