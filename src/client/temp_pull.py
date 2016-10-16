import time
import zmq
import timeit
from threading import Thread
from multiprocessing import Process, Queue
import Queue as Q
temporal_var = {}


def recv_messages(queue):
    while True:
	    print "entre a recv_messages"
	    context = zmq.Context()
	    context_receiver = context.socket(zmq.PULL)
	    context_receiver.connect("tcp://127.0.0.1:5557")      
	    var = context_receiver.recv_json()
	    queue.put(var)
	    print ">> agrege objeto"

def get_list(queue):
    while True:
            #time.sleep()
	    print "entre a get_list"
	    try:
	       print "antes de leer la cola"
	       new_data = queue.get(False)
 	    except Q.Empty:
  	       new_data = {}
	    
	    temporal_var = new_data
	    print "es temporal data para enviar"
	    print temporal_var
	    time.sleep(5)
	    
if __name__ == "__main__":
        queue = Queue()
	try:	
		print queue.get(False)	       
	except Q.Empty:
		print "cola vacia"
	p1 = Process(target = recv_messages, args=((queue),))
	p1.start()	
	p2 = Process(target = get_list, args=((queue),))
        p2.start()
	
