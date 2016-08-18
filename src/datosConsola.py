import pymongo
from bson.json_util import dumps
import matplotlib.pyplot as plt
import numpy as np

client = pymongo.MongoClient()
db = client.prueba

#consultar todos los documentos
#pulsos = db.pulsos.find()
#Consultas filtradas para mejorar la presentacion de la grafica
pulsos = db.pulsos.find({"procesamiento":{"$lt":0.00001}})

for p in pulsos:
	print(p["procesamiento"])