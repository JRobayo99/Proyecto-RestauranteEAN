from tkinter import Tk, Toplevel
from tkinter import *
def main():
    main_window = Tk()
    app = first(main_window)
    main_window.mainloop()


class first:
    def __init__(self, root):
        self.root = root
        self.root.title('First window')

        self.root.geometry('1350x700+0+0')
        frame1 = Frame(self.root, bg='black')
        frame1.place(x=400, y=50, width=400, height=600)
        btn_1 = Button(frame1, command=self.second_window, text='open second window', font=("Times New Roman", 15, 'bold'), bd=3,
                           relief=RIDGE,
                           cursor='hand2', bg='red', fg='white', activeforeground='white', activebackground='red')
        btn_1.place(x=100, y=350, width=220, height=35)

    def second_window(self):
        self.new_window = Toplevel(self.root)
        self.app = second(self.new_window)


class second:
    def __init__(self, root):
        self.root = root
        self.root.title('Second Window')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')
        frame1 = Frame(self.root, bg='black')
        frame1.place(x=400, y=50, width=400, height=600)
        btn_1 = Button(frame1, command=self.first_window, text='open first window',
                       font=("Times New Roman", 15, 'bold'), bd=3,
                       relief=RIDGE,
                       cursor='hand2', bg='red', fg='white', activeforeground='white', activebackground='red')
        btn_1.place(x=100, y=350, width=220, height=35)

    def first_window(self):
        self.new_window = Toplevel(self.root)
        self.app = first(self.new_window)


if __name__ == '__main__':
    main()