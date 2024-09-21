import socket
import asyncio
import tkinter as tk
from PIL import Image, ImageTk
import io
import os

IMAGE_FILE = 'received_screenshot.png'  


async def receive_image(client_socket):
    while True:
        # Receive the image size first
        image_size_data = await asyncio.get_event_loop().run_in_executor(None, client_socket.recv, 4)
        if not image_size_data:
            break
            
        image_size = int.from_bytes(image_size_data, 'big')  # Convert bytes to int
        
        # Receive the actual image data
        image_data = b''
        while len(image_data) < image_size:
            packet = await asyncio.get_event_loop().run_in_executor(None, client_socket.recv, 4096)
            if not packet:
                break
            image_data += packet
        # print("ok")
        # Save the received image data to a file
        with open(IMAGE_FILE, 'wb') as image_file:
            image_file.write(image_data)

async def main():
    host = '192.168.100.166'  # Server's IP address "Do ipconfig in the cmd and see for ipv4 for this"
    port = 5000  # Must match the server's port

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    try:
        # Start the image display loop in a separate task
        # asyncio.create_task(display_image())
        
        await receive_image(client_socket)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    asyncio.run(main())
