# Bluetooth Mesh Network

## Overview
This project implements a comprehensive Bluetooth Mesh Network that allows multiple devices to communicate over a mesh topology.

## Features
- **Scalability**: Supports a wide range of devices.
- **Reliability**: Fault tolerance through mesh networking.
- **Low Energy**: Designed for low energy consumption in embedded systems.

## Quick Start Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/thalha17/bluetooth-mesh-network.git
   cd bluetooth-mesh-network
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Project Structure
```
bluetooth-mesh-network/
│
├── main.py          # Main application file
├── mesh/            # Mesh networking implementations
├── tests/           # Test cases
├── docs/           # Documentation files
└── requirements.txt  # Dependency requirements
```  

## Usage Examples
Here are some examples of how to use the Bluetooth Mesh Network in your projects:
```python
from mesh import MeshNetwork

network = MeshNetwork()
network.add_device(device_id='12345')
network.send_message(to='12345', message='Hello, Mesh!')
```

## Testing
To run the test suite, execute the following:
```bash
pytest tests/
```

## Docker Setup
To set up the project using Docker, follow these steps:
1. Build the Docker image:
   ```bash
   docker build -t bluetooth-mesh-network .
   ```
2. Run the container:
   ```bash
   docker run -it bluetooth-mesh-network
   ```

## Hardware Implementation
This project provides hardware implementations for the following platforms:
- **ESP32**: Use the ESP32 module for Bluetooth connectivity.
- **nRF52840**: Leverage the nRF52840 chip for its mesh capabilities.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.