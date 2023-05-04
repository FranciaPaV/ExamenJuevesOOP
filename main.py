from Coctel import Coctel
from Shots import Shots

opcion = 5
cocteles= []
shots = []

cantidadCocteles = 0
valorVenta = 0

def calcularValor(coctel):
    cantidadcomprada = int(input("Ingrese la cantidad de cocteles: "))
    valorVenta = cantidadcomprada * coctel.precio    

   
    if (coctel.diasHecho > 3):
        print ("El coctel no se puede vender")
    elif(coctel.diasHecho == 3): 
        print(f"El valor del descuento del coctel con tres días es de 50%, por o que vale: {valorVenta * 0.5}")
    elif(coctel.diasHecho == 2):
        print (f"El valor del descuento del coctel con dos días es de 20%, por o que vale: {valorVenta * 0.8}")
    else:
        print(f"El valor es de: {valorVenta}")  

    
def calcularShot(shot):
    cantidadShots = int(input("Ingrese la cantidad de shots: "))   
    valorShot = cantidadShots * shot.precio
    print(f"El costo de los shots es de: {valorShot}")

        
while opcion != 0:
    opcion = int(input("Ingrese 1 para cocteles y 2 para shots: "))
    if(opcion == 1):
        coctel = Coctel()
        coctel.nombre = input("ingrese el nombre del coctel: ")
        coctel.precio = int(input("Ingrese el precio del coctel: "))
        coctel.cantidadAlcohol = int(input("Ingrese cuantos grados de alcohol tiene: "))
        coctel.diasHecho = int(input("Cuantos días llevo hecho: "))
        cocteles.append(coctel)
        calcularValor(coctel)
    elif(opcion == 2):
        shot = Shots()
        shot.nombre = input("ingrese el nombre del shot: ")
        shot.precio = int(input("Ingrese el precio del shot: "))
        shot.gradosalcohol = int(input("Ingrese cuantos grados de alcohol tiene el shot: "))
        shot.temperatura = int(input("Ingrese la temperatura del shot: "))
        shots.append(shot)  
        calcularShot(shot)
    elif(opcion != 1 and opcion != 2):
        print("Gracias por guardar cocteles")

 
