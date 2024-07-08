notas=[45,56,88,90,45,56,78,89,90,45,67] #creamos una lista
promedio=sum(notas)/len(notas)#el promedio es la suma
# de las notas dividido la cantidad (len)
print("El promedio es: ", promedio) #mostramos
nota_mas_baja=min(notas) #min para nota mas baja
nota_mas_alta=max(notas) #max para nota mas alta
print (f"La nota mas baja es: ",nota_mas_baja)
print (f"La nota mas alta es: ",nota_mas_alta)
from collections import Counter 
contador_notas=Counter(notas)
nota_mas_comun=contador_notas.most_common(1)[0][0]
print("La nota más común es: " , nota_mas_comun)
