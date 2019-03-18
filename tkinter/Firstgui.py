from tkinter import Tk, Label, Button, LEFT, RIGHT, W

class MyFirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        #self.label.pack() #standard layout using Pack
        self.label.grid(columnspan=2, sticky=W)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack() #standard layout using Pack
        #self.greet_button.pack(side=LEFT) #offset to left using LEFT; Requires import LEFT
        self.greet_button.grid(row=1) #assigned to row 1 using Grid; Requires import W


        self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack() #standard layout using Pack
        #self.close_button.pack(side=RIGHT) #offset to right using RIGHT; requires import RIGHT
        self.close_button.grid(row=1, column=1) #assigned to row 1 and column 1 using Grid; Requires import W

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
