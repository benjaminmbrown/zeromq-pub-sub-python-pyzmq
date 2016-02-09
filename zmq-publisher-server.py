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
	# topic is zipcode, default is NYC, 10001
	topic = random.randrange(9999,10005)
	#our mock data is weather temps
	messagedata = random.randrange(1,215)-80;
	print "%d %d" % (topic, messagedata)
	socket.send("%d %d" % (topic, messagedata))
	time.sleep(1)