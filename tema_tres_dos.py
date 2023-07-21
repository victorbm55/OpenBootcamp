#Ejercicio 2 tema 3 Introducción a la programación

#Crear una clase coche.

#Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.

#Una función que incremente el número de puertas que tiene el coche.

#Crear un objeto miCoche en el main y añadirle una puerta.

#Mostrar el número de puertas que tiene el objeto.

class coche:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas
       
        
    def añadir_puerta(self):
        
        self.num_puertas += 1  


micoche = coche(0)

  
micoche.añadir_puerta()

print("Mi coche tiene", micoche.num_puertas, "puertas.")

  
  
  



    





