# -*- coding: utf-8 -*-
#!/sr/lib/python
import timeit
import sys
import Adafruit_DHT
import datetime
import zmq

while True:
    try: 
	    start = timeit.default_timer()   
	    humidity, temperature = Adafruit_DHT.read_retry(11,4)
	    var = 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)
	    a = datetime.datetime.now().strftime("%H:%M:%S:%f")
	    print a + var
	    data = {"var_temp_humidity":var,"hora_fecha":a}
	    #zmq process
	    context = zmq.Context()
	    zmq_socket = context.socket(zmq.PUSH)
	    zmq_socket.bind("tcp://127.0.0.1:5557")
	    zmq_socket.send_json(data)
	    stop = timeit.default_timer()
	    print ("diferencia: ")
            print (stop - start)
    except KeyboardInterrupt:
            exit()
    except:
	    pass

