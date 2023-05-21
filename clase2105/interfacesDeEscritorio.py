import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.title("mi app")
root.geometry('500x500')


def getdata():
    data=entrydata.get()
    print(data)
    if "CAMBIO"==data.upper():
        messagebox.showerror('error','ingrese un dato correcto')
    else:
        result=messagebox.askyesno('consulta',"desea guaradar los cambios")
        print(result)

label1=tkinter.Label(root,text="hello word")
label1.grid(row=0,column=0,sticky="w")
entrydata=tkinter.Entry(root)
#entrydata.pack()
entrydata.grid(row=0,column=2,sticky="e")

buttonsend=tkinter.Button(root,text="envair data",bg="#000",fg='white',font=('Arial',10),command=getdata)
buttonsend.grid(row=1,column=1)
root.mainloop()