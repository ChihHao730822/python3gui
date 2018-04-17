from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class window():

    def __init__(self):
        self.win = Tk()
        self.win.title("test")
        self.win.geometry("830x700")
        self.win.resizable(0,0)
        self.win.protocol("WM_DELETE_WINDOW",self.on_exit)

        self.win2=Tk()


        menuBar=Menu(self.win)
        self.win.config(menu=menuBar)

        #Create a pull-down menu, and add it to menu bar
        operationMenu=Menu(self.win, tearoff=0)
        menuBar.add_cascade(label="Operation", menu=operationMenu)
        operationMenu.add_command(label="Save log", command='')
        operationMenu.add_command(label="Open", command='')
        operationMenu.add_separator()
        operationMenu.add_command(label="Exit", command=self.on_exit)

        #about menu
        aboutMenu=Menu(self.win,tearoff=0)
        menuBar.add_cascade(label="About", menu=aboutMenu)
        aboutMenu.add_command(label="Arthuor", command=self.showAuthor)

        secAboutMenu=Menu(self.win, tearoff=0)
        aboutMenu.add_cascade(label="second layer", menu=secAboutMenu)
        secAboutMenu.add_command(label="test1")


        frame1=Frame(self.win)
        frame1.grid(row=0,column=0, sticky=N)
        lb=Label(frame1,text="Searial Port")
        lb.grid(row=0, column=0,columnspan=5)
        text = Text(frame1, width=25, height=30, state="disabled")
        text.grid(row=1, column=0,columnspan=5)

        lbBaudRate=Label(frame1,text="BaudRate :")
        lbBaudRate.grid(row=2,column=0, sticky=E+W)
        cobBaudRate=ttk.Combobox(frame1,width=10,state="readonly",value=("115200","9600"))
        cobBaudRate.grid(row=2,column=1, sticky=E+W)

        lbParity=Label(frame1,text="Parity :")
        lbParity.grid(row=3,column=0, sticky=E+W)
        cobParity=ttk.Combobox(frame1,width=10,state="readonly",value=("None", "Odd","Even"))
        cobParity.grid(row=3,column=1)

        lbDataBit = Label(frame1, text="DataBit :")
        lbDataBit.grid(row=4, column=0, sticky=E+W)
        cobDataBit = ttk.Combobox(frame1, width=10,state="readonly",value="8")
        cobDataBit.grid(row=4, column=1)

        lbStopBit = Label(frame1, text="StopBit :")
        lbStopBit.grid(row=5, column=0, sticky=E+W)
        cobStopBit = ttk.Combobox(frame1, width=10,state="readonly",value=("1","2"))
        cobStopBit.grid(row=5, column=1)

        self.btn1=Button(frame1, text="click me", width=20)
        self.btn1.grid(row=6, column=0, rowspan=3, columnspan=10, sticky=S)
        self.btn2=Button(frame1, text="click me 2", width=20, command=self.click)
        self.btn2.grid(row=9, column=0, rowspan=3, columnspan=10, sticky=S)



        frame2=Frame(self.win,width=100)
        frame2.grid(row=0,column=1)
        scb = Scrollbar(frame2)
        scb.grid(row=0, column=7)
        self.listb=Listbox(frame2, width=70, height=40,yscrollcommand=scb.set, state="disabled")
        scb['command']=self.listb.yview
        self.listb.grid(row=0,column=1, columnspan=5, sticky=W+E)

        entrybox=Entry(frame2,width=70)
        entrybox.grid(row=1,column=1, sticky=W+E)

        self.btnSend = Button(frame2, text="Send")
        self.btnSend.grid(row=1,column=2, sticky=W)

        lbMessage=Label(frame2,width=70,text="Messages")
        lbMessage.grid(row=10,column=1, sticky=S+W,rowspan=50)

        self.win.mainloop()
        self.win2.mainloop()
    def on_exit(self):
        if messagebox.askyesno("Exit","Rellay quit?"):
            self.win.destroy()
            self.win2.destroy()

    def click(self):
        if self.btn1['state']=="disabled":
            self.btn1.config(state="normal")
            self.listb.insert(END,"on")
        else:
            self.btn1.config(state="disabled")

    def showAuthor(self):
        messagebox.showinfo("Author", "     Lain          ")



if __name__=='__main__':
    window()
