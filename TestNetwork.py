import sys
import time
import ClientNode
import socket
import sendFile as sendFile

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
id = socket.gethostname()
s.close()

MainNodeIP = "10.10.2.192"


node = ClientNode.ClientNode(ip, 10002, id)
# node2 = ClientNode.ClientNode("127.0.0.1", 10002, id)
time.sleep(1)

# Do not forget to start your node!
node.start()
# node2.start()
time.sleep(5)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node(MainNodeIP, 10001)
time.sleep(2)

# Example of sending a message to the nodes (dict).
# node.send_to_nodes({"message": "Hi there!"})

sendFile.sendFile('test.txt')

time.sleep(5) # Create here your main loop of the application

node.stop()
# node2.stop()