# zeromq-pub-sub-python-pyzmq
Classic pub/sub pattern in zeromq &amp; python
<br/>
Publishers of messages publish them without knowledge of any subscribers. Subscribers can connect to multiple publishers.

<br/>
To run start two publisher servers:<br/>
python zmq-publisher-server.py 5546<br/>
python zmq-publisher-server.py 5546<br/>
And create subscriber that is subscribed to both<br/>
python zmq-subscriber-client.py 5546 5556<br/>