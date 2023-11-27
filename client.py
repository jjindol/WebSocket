import socket
import tkinter as tk
from tkinter import simpledialog

def send_data_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.7', 8011))
    
    while True:
        # Get user input from GUI
        user_input = simpledialog.askstring("Input", "계속하실건가요? (yes/no)",
                                    parent=application_window)
        if user_input is None: # If the dialog is canceled, return
            break

        client.send(user_input.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        text_widget.insert(tk.END, response)

# Create the main window
application_window = tk.Tk()

# Create a text widget
text_widget = tk.Text(application_window)
text_widget.pack()

# Create a button that will call the send_data_to_server function
button = tk.Button(application_window, text="Send", command=send_data_to_server)
button.pack()

# Run the Tkinter event loop
application_window.mainloop()
