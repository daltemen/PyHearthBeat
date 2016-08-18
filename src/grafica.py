import pymongo
from bson.json_util import dumps
import matplotlib.pyplot as plt
import numpy as np

client = pymongo.MongoClient()
db = client.prueba

#consultar todos los documentos
pulsos = db.pulsos.find()
#Consultas filtradas para mejorar la presentacion de la grafica
#pulsos = db.pulsos.find({"procesamiento":{"$lt":0.00001}})
tiemposProcesamiento = []

#Se guarda solo el atributo con el que se va a trabajar
for p in pulsos:
	tiemposProcesamiento.append(p["procesamiento"])
	
#se define el eje x que son la cantidad de elementos
x = np.arange(1,len(tiemposProcesamiento)+1,1)
#grafica
plt.plot(x,tiemposProcesamiento, 'ro')
plt.show()