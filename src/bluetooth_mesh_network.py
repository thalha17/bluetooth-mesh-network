# Bluetooth Mesh Network Implementation

class BluetoothMeshNetwork:
    def __init__(self):
        self.nodes = []
        self.network = ""

    def add_node(self, node):
        """Add a new node to the network."""
        self.nodes.append(node)
        self.network += f"Node {node} added.\n"

    def remove_node(self, node):
        """Remove a node from the network."""
        if node in self.nodes:
            self.nodes.remove(node)
            self.network += f"Node {node} removed.\n"
        else:
            print(f"Node {node} not found in the network.")

    def send_message(self, message):
        """Send a message to all nodes in the network."""
        for node in self.nodes:
            print(f"Sending message to {node}: {message}")

    def __str__(self):
        return f"BluetoothMeshNetwork with {len(self.nodes)} nodes.\n" + self.network

# Example usage:
if __name__ == '__main__':
    bmn = BluetoothMeshNetwork()
    bmn.add_node("Node1")
    bmn.add_node("Node2")
    bmn.send_message("Hello Mesh Network!")
    print(bmn)