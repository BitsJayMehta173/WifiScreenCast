import tkinter as tk
import subprocess
import os

def run_script(script_name):
    # Adjust the path to your scripts as necessary
    script_path = os.path.join(os.getcwd(), script_name)
    subprocess.Popen(['python', script_path])

def on_selection(choice):
    if choice == 'Sender':
        run_script('sender.py')  # Change this to your sender script name
    elif choice == 'Receiver':
        run_script('receiver.py')  # Change this to your receiver script name

# Create the main window
root = tk.Tk()
root.title("Select Mode")

# Create a label
label = tk.Label(root, text="Choose Sender or Receiver:")
label.pack(pady=10)

# Create buttons for Sender and Receiver
btn_sender = tk.Button(root, text="Sender", command=lambda: on_selection('Sender'))
btn_sender.pack(pady=5)

btn_receiver = tk.Button(root, text="Receiver", command=lambda: on_selection('Receiver'))
btn_receiver.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
