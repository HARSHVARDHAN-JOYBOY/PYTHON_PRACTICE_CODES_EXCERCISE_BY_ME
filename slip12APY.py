import tkinter as tk
from tkinter import font

def updatefont():
    selectedf=fontname.get()
    size=int(fontsize.get())
    weight= 'bold' if boldf.get() else 'normal'
    label.config(font=(selectedf,size,weight))

root=tk.Tk()
root.title("font style changer")
root.geometry("300x200")

fontname=tk.StringVar(value="Arial")
boldf=tk.BooleanVar()
fontsize=tk.IntVar(value=12)

label=tk.Label(root,text="sample text" ,font=("Arial",12))
label.pack(pady=10)

selectedf=tk.Label(root,text="select font:")
selectedf.pack()
fontnamemenu=tk.OptionMenu(root,fontname,"Arial","Times New Roman","Courier")
fontnamemenu.pack()

fontsizel=tk.Label(root,text="Enter font size: ")
fontsizel.pack()
fontsize=tk.Entry(root)
fontsize.pack()
fontsize.insert(0,"12")

boldcheck=tk.Checkbutton(root,text="Bold",variable=boldf,command=updatefont)
boldcheck.pack()

updatebutton=tk.Button(root,text="Update font",command=updatefont)
updatebutton.pack(pady=10)

root.mainloop()
