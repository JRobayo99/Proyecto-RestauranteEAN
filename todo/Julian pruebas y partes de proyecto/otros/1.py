import tkinter 
import tkinter as tk

class Demo1:
    
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Menu del día', width = 80, command = self.new_window)
        self.button1.place(x=300,y=300)
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    

class Demo2:
    def __init__(self, master):
       
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Volver a inicio', width = 80, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Demo12:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,text="Aparta tu mesa",width=80,command = self.new_window) 
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo22:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Volver a inicio', width = 80, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Demo32:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,text="Inventario",width=80,command = self.new_window) 
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo23:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Volver a incio', width = 80, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Demo42:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,text="Registro de empleados",command = self.new_window,width=80)
        
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo24:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Volver a incio', width = 80, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main(): 
    root=tk.Tk()
    root.geometry=("3000x3000")
    app = Demo1(root)
    app= Demo12(root)
    app=Demo32(root)
    app=Demo42(root)
    root.mainloop()

if __name__ == '__main__':
    main()
