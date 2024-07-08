#realizar un gráfico de barras con las notas
import matplotlib.pyplot as plt #importamos la biblioteca
#matplotlib para crear gráficos
from collections import Counter #importamos Counter del módulo collectons
notas=[45,56,88,90,45,56,78,89,90,45,67]
#contar la frecuencia de cada nota
contador_notas=Counter(notas)
#separar las notas y sus frecuencias para el gráfico
notas_unicas=list(contador_notas.keys()) #buscamos las 
#notas únicas (keys)
frecuencia=list(contador_notas.values()) #las notas frecuentes
#creando gráfico de barras
plt.title("Frecuencia de notas") #título del gráfico
plt.xlabel("Notas") #etiqueta eje x
plt.ylabel("Frecuencia") #etiqueta eje y
#Mostramos el gráfico
plt.show()