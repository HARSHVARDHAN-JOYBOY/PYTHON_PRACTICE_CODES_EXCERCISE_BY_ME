import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title and size
root.title("Hello, Tkinter!")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Add a button widget
button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()

# Run the Tkinter event loop
root.mainloop()
