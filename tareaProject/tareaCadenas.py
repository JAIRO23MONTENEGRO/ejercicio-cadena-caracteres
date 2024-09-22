"""""
name = "Luiz"
age = str(27)
favouriteFood  = "Pasta con salsa Boloñesa"
fullInformacion= "Hola! Mi nombre es "+name+". Yo tengo "+ age+" años, y mi comida favorita es "+favouriteFood
print(fullInformacion)
#Solicitar el nombre al usuario
name1 = input("Ingresa tu nombre completo")
name1SinEspacios= name1.replace(" ","")
cantidadLetras = len(name1SinEspacios)
print(f"Hola,{name1}! Tu nombre tiene {cantidadLetras} letras, excluyendo los espacios.")
"""""

increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078

# Formatear los porcentajes a dos decimales
increaseSalesFormatted = f"{increaseSalesPercent:.2f}%"
revenueGrowthFormatted = f"{revenueGrowthPercent:.2f}%"

# Generar la cadena con los porcentajes formateados
porcentajeM = (f"Las ventas de la empresa láctea aumentaron un {increaseSalesFormatted} "
           f"y los ingresos crecieron un {revenueGrowthFormatted}.")

print(porcentajeM)
