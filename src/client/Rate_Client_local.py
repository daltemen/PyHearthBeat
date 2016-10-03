from threading import Timer
import timeit
import datetime
import time
import os 
import websocket
import json

def recibir_pulso():
    try:
        while True:
            start = timeit.default_timer()
            
            time.sleep(2)
            ws.send(json.dumps({"var":1}))
            time.sleep(1)
            ws.send(json.dumps({"var":0}))
            
            stop = timeit.default_timer()
            
            print (stop - start)
            print (datetime.datetime.now().strftime("%H:%M:%S:%f"))

            #print("Receiving...")
            #result = ws.recv()
            #print("Received {}".format(result))
    except KeyboardInterrupt:
        print ("Received Interrupt") 

websocket.enableTrace(True)
ws = websocket.create_connection("ws://localhost:3000/websocket")
Timer(1, recibir_pulso()).start()
