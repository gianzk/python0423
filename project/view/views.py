from controller.UserController import * 
from tkinter import Tk ,Frame,Label,Entry,Button,messagebox
import bcrypt

class Views(Tk):

    def __init__(self):
        self.rootMain=Tk()
        self.name=[]
        self.frames={}
    def config(self,**kw):
        if 'title' in kw:
            self.rootMain.title(kw['title'])
        if 'icon' in kw:
            self.rootMain.iconbitmap(kw['icon'])
        if 'size' in kw:
            self.rootMain.geometry(kw['size'])
    def showFrame(self,frame):
        pass
    def deleteFrame(self,frameTitle):
        pass

    def listenEvent(self):
        pass

    def run(self):
        self.rootMain.mainloop()

class Dashboard(Frame):
    def __init__(self,frameP):
        self.frameRootParent=frameP
        self.frameRoot=Frame(frameP,width=400,height=200,name="topDashboard")
        self.labelUser=Label(self.frameRoot,text='Dasboard:')
        self.labelUser.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.userEntry=Entry(self.frameRoot)
        self.userEntry.grid(row=0,column=1,padx=10,pady=10,sticky="e")
        self.frameRoot.pack(pady=50)
    def getHeader():
        pass

    def getTable():
        pass
        
class Login(Frame):
    def __init__(self,frameP):
        self.frameRootParent=frameP
        self.frameRoot=Frame(frameP,width=400,height=400,name="login")        
        self.labelUser=Label(self.frameRoot,text='User:')
        self.labelUser.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.userEntry=Entry(self.frameRoot)
        self.userEntry.grid(row=0,column=1,padx=10,pady=10,sticky="e")
        self.labelPassword=Label(self.frameRoot,text='Password:')
        self.labelPassword.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        self.passwordEntry=Entry(self.frameRoot,show='*')
        self.passwordEntry.grid(row=1,column=1,padx=10,pady=10,sticky="e")
        self.loginButton=Button(self.frameRoot,text="Iniciar session",command=lambda:self.loginSession())
        self.loginButton.grid(row=2,columnspan=2)
        self.frameRoot.pack(pady=50)
    def loginSession(self):
        user=self.userEntry.get()
        passw=self.passwordEntry.get()
        ctrl=UserController()
        data=ctrl.getUser(user)
        print(data,"=>",passw)
        print("login init")
        if bcrypt.checkpw(passw.encode("utf-8"),data[2]):
            self.frameRoot.pack_forget()
            d1=Dashboard(self.frameRootParent)
        else:
            self.viewMessageError({"title":'Login',"description":"error al loguearse"})
    def viewMessageError(self,message):
        messagebox.showerror(message['title'],message['description'])


def startApp():
    app=Views()
    app.config(title='app1',size="800x800")
    login=Login(app.rootMain)
    app.run()
