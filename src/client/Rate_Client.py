from threading import Timer
import timeit
import datetime
import time
import RPi.GPIO as io 
import os 
import websocket
import json

def recibir_pulso():
    io.setmode(io.BCM)
    io.setwarnings(False)

    receiver_in = 23
    LED_in = 24

    io.setup(receiver_in, io.IN) 
    io.setup(LED_in, io.OUT)  
    io.output(LED_in, io.HIGH) 

    sample=2
    oldSample=1
    try:
        while True:
            start = timeit.default_timer()
            sample = io.input(receiver_in)
            if sample == 1 and oldSample == 0:
                print "Beat 1"
                ws.send(json.dumps({"var":1}))
                #io.output(LED_in, io.LOW)
                print("Receiving...")
                result = ws.recv()
                print("Received {}".format(result))
                
            if sample == 0 and oldSample == 1:
                print "Beat 0"
                ws.send(json.dumps({"var":0}))
                #io.o   dsfutput(LED_in, io.HIGH) # turn LED off
                print("Receiving...")
                result = ws.recv()
                print("Received {}".format(result))
            stop = timeit.default_timer()
            print (stop - start)   
            print (datetime.datetime.now().strftime("%H:%M:%S:%f"))
            oldSample = sample
    except KeyboardInterrupt:
        print "Received Interrupt" 
"""
def recibir_pulso():
    try:
        while True:
            start = timeit.default_timer()
            
            time.sleep(1)
            ws.send(json.dumps({"var":1}))
            time.sleep(0.5)
            ws.send(json.dumps({"var":0}))
            
            stop = timeit.default_timer()
            
            print (stop - start)
            print (datetime.datetime.now().strftime("%H:%M:%S:%f"))

            #print("Receiving...")
            #result = ws.recv()
            #print("Received {}".format(result))
    except KeyboardInterrupt:
        print ("Received Interrupt") 
"""
websocket.enableTrace(True)
ws = websocket.create_connection("ws://52.43.170.107:3000/websocket")
Timer(1, recibir_pulso()).start()
