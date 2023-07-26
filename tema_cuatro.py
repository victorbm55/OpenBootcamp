#Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
#Pista: Los números inferiores a 0 son negativos y los superiores, positivos.

#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
#Incrementar el valor de la variable en uno cada vez que se ejecute.
#Mostrarlo por pantalla cada vez que se ejecute.

#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

#Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

#Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.

#Primer ejercicio

###numeroif = 0

###if numeroif == 0:
   ### print(f"El número es 0")  
    
###elif numeroif < 0:
   ### print("El número es negativo")
    
###else:
    ###print("El número es positivo")    
    
      
#Segundo ejercicio

###numero_while = -5

###while numero_while < 3:
    ###print(numero_while)
    ###numero_while += 1
    
    
#Tercer ejercicio "He tenido que buscar como hacer una especie de do while con python"

###numero_while = -5

###while True: 
    ###print(numero_while) 
    ###numero_while += 1 
    ###if numero_while != -5: 
        ###break
        
#Cuarto ejercico

###numerofor = 0
###for i in range(4):
    ###print(numerofor)
    ###numerofor += 1
    
#Quinto ejercicio

def informar_estacion(estacion):
    mens_estacion = {
        "primavera": "Estamos en primavera",
        "verano": "Estamos en verano",
        "otoño": "Estamos en otoño",
        "invierno": "Estamos en invierno"
    }
    mensaje = mens_estacion.get(estacion, "La estación no es válida")
    print(mensaje)

informar_estacion("invierno")

























