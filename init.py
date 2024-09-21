import tkinter as tk
from tkinter import Label
import subprocess
import os
import threading
import time
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Viewer")
        
        self.label = Label(root)
        self.label.pack(pady=20)
        
        self.image_path = "received_screenshot.png"
        
        # Start the image update loop in a separate thread
        self.update_image_thread = threading.Thread(target=self.update_image)
        self.update_image_thread.daemon = True
        self.update_image_thread.start()

    def update_image(self):
        while True:
            if os.path.exists(self.image_path):
                try:
                    # Attempt to open and display the image
                    image = Image.open(self.image_path)
                    image.thumbnail((800, 600))  # Resize if needed
                    photo = ImageTk.PhotoImage(image)

                    self.label.config(image=photo)
                    self.label.image = photo  # Keep a reference
                except Exception as e:
                    print(f"Error loading image: {e}")
                    # Optionally, clear the label if there's an error
                    self.label.config(image=None)

            # time.sleep(1)  # Check for the file every second

def run_script(script_name):
    script_path = os.path.join(os.getcwd(), script_name)
    subprocess.Popen(['python', script_path])

def on_selection(choice):
    if choice == 'Sender':
        run_script('./sender/sender.py')  # Change this to your sender script name
    elif choice == 'Receiver':
        run_script('./receiver/receiver.py')  # Change this to your receiver script namez

def create_main_window():
    root = tk.Tk()
    root.title("Select Mode")

    label = tk.Label(root, text="Choose Sender or Receiver:")
    label.pack(pady=10)

    btn_sender = tk.Button(root, text="Sender", command=lambda: on_selection('Sender'))
    btn_sender.pack(pady=5)

    btn_receiver = tk.Button(root, text="Receiver", command=lambda: on_selection('Receiver'))
    btn_receiver.pack(pady=5)

    return root

if __name__ == "__main__":
    main_window = create_main_window()
    app = ImageDisplayApp(main_window)
    main_window.mainloop()
