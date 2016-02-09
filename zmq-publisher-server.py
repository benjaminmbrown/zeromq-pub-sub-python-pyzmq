import zmq
import random
import sys
import time

port = "5556"

if len(sys.argv)>1:
	port = sys.argv[1]
	print "port: ", port
	int(port)

context= zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

#publish data w/ a topic the subscribers can usually 
#filter on topics

while True:
	topic = random.randrange(999,1020)
	messagedata = random.randrange(1,100)
	print "%d %d" % (topic, messagedata)
	socket.send("%d %d" % (topic, messagedata))
	time.sleep(1)