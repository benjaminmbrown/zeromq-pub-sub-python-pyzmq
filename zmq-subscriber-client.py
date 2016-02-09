import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
	port = sys.argv[1]
	int(port)

if len(sys.argv) > 2:
	port1 = sys.argv[2]
	int(port1)

#open socket to tlak to publisher server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Getting updates from server..."
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
	socket.connect("tcp://localhost:%s" % port1)


#filter messages based on topic
topicfilter = "10001"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

#show some updates
total_val = 0
for update_nbr in range(25):
	string = socket.recv()
	print 'socket string', string
	topic,messagedata = string.split()
	total_val += int(messagedata)
	print "Zip: ",topic, "Temp: ", messagedata

print "Average temp for zip '%s' was %dF" % (topicfilter, total_val/update_nbr)