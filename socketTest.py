import socket

def send_command(ip, port):
    # Frame components
    STX = b'\x02'  # Start of Text (02h)
    ETX = b'\x03'  # End of Text (03h)
    seq_no = b"000"  # Sequence number (3 ASCII digits)
    command = b"Z"  # Command
    data_length = b"0001"  # Length of the command (4 ASCII digits)

    # Construct the full command frame
    frame = STX + seq_no + data_length + command + ETX

    try:
        print(f"Connecting to {ip}:{port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(30)  # Set a timeout
            s.connect((ip, port))
            print("Connection established")
            
            # Send the frame
            s.sendall(frame)
            print(f"Sent frame: {frame}")

            # Receive the response
            response = s.recv(1024)
            print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_command("172.16.10.100", 5003)
