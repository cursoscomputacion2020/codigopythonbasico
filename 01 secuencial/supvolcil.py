# Propósito: Determinar el área y el volumen de un cilindro
# Autor:     Alejandro Bolívar
# Fecha:     30/01/2020


# Entrada de datos
radio = float(input('Radio de la base:'))
altura = float(input('Altura del cilindro: '))

# Procesamiento de datos
area = 3.141516 * radio * radio
volumen = (2 * 3.141516 * radio) * altura

#Salida de datos
print("Area del Cilindro= ", area)
print("Volumen del Cilindro= ", volumen)

# Fin del programa
input('Pulse una tecla para finalizar... ') # Pausa

