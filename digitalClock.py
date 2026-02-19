# import tkinter as tk
# from time import strftime
# from PIL import Image, ImageTk

# root=tk.Tk()
# root.title("Digital Clock By Harshvardhan")
# def time():
#     string= strftime('%H:%M:%S %p \n %D:%M:%Y')
#     label.config(text=string)
#     label.after(1000,time)

# imgge=Image.open("rk.jpg")
# imgge= imgge.resize((600,400))
# img=ImageTk.PhotoImage(imgge)

# bg_label = tk.Label(root, image=img)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# label=tk.Label(root,font=('calibri',50,'bold'),background=None  ,foreground='white')    
# label.place(relx=0.5, rely=0.5, anchor='center')

# time()
# root.mainloop()



import tkinter as tk
from time import strftime
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Digital Clock By Harshvardhan")

# Load and resize the background image
image = Image.open("rk.jpg")
image = image.resize((600, 400))
bg_image = ImageTk.PhotoImage(image)

# Create canvas and add image
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Add text to canvas (no background!)
text_item = canvas.create_text(300, 200, text="", font=('calibri', 40, 'bold'), fill="white", justify="center")

# Function to update the time
def time():
    string = strftime('%I:%M:%S %p\n%m/%d/%Y')
    canvas.itemconfig(text_item, text=string)
    root.after(1000, time)

time()
root.mainloop()
