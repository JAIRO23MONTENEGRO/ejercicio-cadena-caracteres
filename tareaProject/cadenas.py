from queue import PriorityQueue
from string import punctuation
from tkinter.constants import CENTER

punto1="PUNTO 1. →genera una cadena para presentarse";print(punto1.center(120,"•"))
name = "Luiz"
age = str(27)
favouriteFood  = "Pasta con salsa Boloñesa"
fullInformacion= "Hola! Mi nombre es "+name+". Yo tengo "+ age+" años, y mi comida favorita es "+favouriteFood+ "\n"
print(fullInformacion)
punto2="PUNTO 2. →saludar al usuario e informarle la longitud de su nombre";print(punto2.center(120,"•"))
#Solicitar el nombre al usuario
name1 = input("Ingresa tu nombre completo:\n|")
name1SinEspacios= name1.replace(" ","")
cantidadLetras = len(name1SinEspacios)
print(f"Hola, {name1}! Tu nombre tiene {cantidadLetras} letras, excluyendo los espacios.\n")
punto3="PUNTO 3. →cadena para mostrar los porcentajes de aumento de ventas y crecimiento de ingresos";print(punto3.center(120,"•"))
from http.cookiejar import join_header_words
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
# Formatear los porcentajes a dos decimales
porcentajeVentas = f"{increaseSalesPercent:.2f}%"
porcentajeIngresos = f"{revenueGrowthPercent:.2f}%"
# Generar la cadena con los porcentajes formateados
print(f"Las ventas de la empresa láctea aumentaron un {porcentajeVentas} "
           f"y los ingresos crecieron un {porcentajeIngresos}.\n")

punto4="PUNTO 4. →mensaje secreto";print(punto4.center(120,"•"))
secretMessage = "aS!Ir waQm VL!eDafrcnXin=gS .P,yytahgoln.!"
n=3 #variable inicial para el conteo
contador=1 #acumulador para sumar desplazarnos sobre el mensaje después de cada caracter encontrado sin contar cada vez
caracter1=secretMessage[n:n+1];contador=contador+n
caracter2=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter3=secretMessage[contador+n:contador+n+1];contador=contador+n
caracter4=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter5=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter6=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter7=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter8=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter9=secretMessage[contador+n:contador+n+1];contador=contador+1
caracter10=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter11=secretMessage[contador+n:contador+n+1];contador=contador+n+1
caracter12=secretMessage[contador+n:contador+n+1];contador=contador+n
caracter13=secretMessage[contador+n:contador+n+1];contador=contador+1
caracter14=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter15=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter16=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter17=secretMessage[contador+n:contador+n+1];contador=contador+2
caracter18=secretMessage[contador+n:contador+n+1];contador=contador+n
caracter19=secretMessage[contador+n:contador+n+1]
print(f"{caracter1} {caracter2}{caracter3} {caracter4}{caracter5}{caracter6}"
      f"{caracter7}{caracter8}{caracter9}{caracter10}{caracter11} {caracter12}"
      f"{caracter13}{caracter14}{caracter15}{caracter16}{caracter17}{caracter18}\n")

punto5="PUNTO 5. →mostrar el número de palabras en una frase";print(punto5.center(120,"•"))
text = "El nombre 'Python' viene dado por la afición de Van Rossum al grupo Monty Python"
separar=text.split()
print(f"Numero de palabras en la frase: {len(separar)}\n")

punto6="PUNTO 6. →CAMILA POR CEMILE, reemplazar 'a' por 'e'";print(punto6.center(120, "•"))
word="Camila"
print(word.replace("a","e")+"\n")

punto7="PUNTO 7. →Invertir el orden de las palabras";print(punto7.center(120,"•"))#escriba un programa que invierta el orden de las palabras
sentence = "La historia del lenguaje de programación Python"
separar_palabras=sentence.split()
separador=" "
orden=separar_palabras[::-1]
unir=separador.join(orden)
print(unir)