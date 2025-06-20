
import socket
import tkinter

def get_ip_address():
 hostname = socket.gethostname()
 ip_address = socket.gethostbyname(hostname)
 return ip_address

# Create the main window
root = tkinter.Tk()
root.title("IP Address")
root.geometry("240x60")

# Create a label with hover event
ip_address = get_ip_address()
label = tkinter.Label(root, text=f"Your IP Address is: {ip_address}")
label.pack(pady=20)

# Run the application
root.mainloop()
