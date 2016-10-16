import os
import time
from datetime import datetime
import pymongo
from bson.json_util import dumps

from celery import Celery

#Conectarse al broker message RABBITMQ
celery = Celery("tasks", broker="amqp://guest:guest@localhost//")
celery.conf.CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'amqp')
con = pymongo.MongoClient()
database = con["prueba"]

@celery.task
def guardar_Data(mensaje, llegada):
    if "var" in mensaje:
        insert = database.pulsos.insert({
                                    "valor": mensaje["var"],
				    "temperatura_humedad" : mensaje["temp_hum"],				    
                                    "llegada": llegada
                                 })
        print (mensaje["cont"])
    else:
        print ("invalido")

if __name__ == "__main__":
    celery.start()
