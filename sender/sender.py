import socket
import time
from PIL import ImageGrab
import io

def server_program():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 5000  # Arbitrary port number

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on port {port}")

    # Accept a client connection
    conn, address = server_socket.accept()
    print(f"Connection established with {address}")

    try:
        while True:
            # Capture a screenshot
            screenshot = ImageGrab.grab()
            with io.BytesIO() as output:
                screenshot.save(output, format='PNG')
                image_data = output.getvalue()
                
            # Send the image size first
            conn.sendall(len(image_data).to_bytes(4, 'big'))  # Send image size (4 bytes)
            conn.sendall(image_data)  # Send the image data

            print("Screenshot sent to client")
            # time.sleep(1)  # Wait for 1 second before sending the next screenshot
    except KeyboardInterrupt:
        print("Server stopped manually.")
    finally:
        conn.close()

if __name__ == '__main__':
    server_program()