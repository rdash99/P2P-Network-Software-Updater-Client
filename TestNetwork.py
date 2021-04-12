import sys
import time
import ClientNode
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
id = socket.gethostname()
s.close()

MainNodeIP = "192.168.1.219"

Connected = False

node = ClientNode.ClientNode(ip, 10002, id)
# node2 = ClientNode.ClientNode("127.0.0.1", 10002, id)
time.sleep(1)

# Do not forget to start your node!
node.start()
# node2.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
while Connected == False:
    try:
        node.connect_with_node(MainNodeIP, 10001)
        Connected = True
    except:
        print("Trying to connect to " + MainNodeIP)
        Connected = False
time.sleep(2)

# Example of sending a message to the nodes (dict).
# node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()
# node2.stop()