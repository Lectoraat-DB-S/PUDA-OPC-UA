from opcua import Client
import json
import time

# Replace 'opc.tcp://<OPC_SERVER_IP>:4840/freeopcua/server/' with the actual server address
server_address = 'opc.tcp://10.38.4.227:4840/freeopcua/server/'

# Create a connection to the OPC UA server
client = Client(server_address)
client.connect()


try:
    while(1):
        # Find the variable node (MyVariable) in the server's address space
        node = client.get_node("ns=2;i=2")  
        node2 = client.get_node("ns=2;i=3")
        node3 = client.get_node("ns=2;i=4")

        # Read the current value of the variable
        current_value = node.get_value()
        current_value2 = node2.get_value()
        current_value3 = node3.get_value()
        print("Current Value:", current_value)
        print("Current Value2:", current_value2)
        print("Current Value3:", current_value3)
        print("--------------------------")

        #Save the value to a file (or database, etc.)
        with open("opcua_variable_value.json", "w") as file:
            file.write((current_value2))
            print(json.dumps(current_value3))
        time.sleep(1)

finally:
    # Disconnect from the OPC UA server
    client.disconnect()