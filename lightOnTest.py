import socket

def send_command(ip, port, command):
    """
    Generic function to send a command to the controller.
    """
    STX = b'\x02'  # Start of Text
    ETX = b'\x03'  # End of Text
    seq_no = b"087"  # Sequence number (replace as needed)
    data_length = f"{len(command):04}".encode()  # Calculate the command length

    # Construct the command frame
    frame = STX + seq_no + data_length + command.encode() + ETX

    try:
        print(f"Connecting to {ip}:{port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # Set timeout
            s.connect((ip, port))
            print("Connection established")
            
            # Send the command frame
            s.sendall(frame)
            print(f"Sent frame: {frame}")

            # Receive the response
            response = s.recv(1024)
            print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")

def turn_on_light(ip, port):
    """
    Function to send the specific command to turn on a particular light.
    """
    # Command to turn on the light
    command = "P100000988888"  # Replace with your specific light control command
    send_command(ip, port, command)

if __name__ == "__main__":
    controller_ip = "172.16.10.100"  # Replace with the actual controller IP
    controller_port = 5003  # Replace with the actual controller port

    # Call the function to turn on the light
    turn_on_light(controller_ip, controller_port)
