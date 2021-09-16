
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super(). __init__(master)
        self.master = master
        self.pack()
        self.creative_widgets()
    def creative_widgets(self):
        self.hi_there= tk.Button(self)
        self.hi_there["text"]= "Hola mundo\n(clikea)"
        self.hi_there["command"]= self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT",fg="red", command= self.master.destroy)

        self.quit.pack(side="bottom")
    def say_hi(self):
        print("Hola, Hola")
root= tk.Tk()
app = Application(master=root)
app.mainloop()
