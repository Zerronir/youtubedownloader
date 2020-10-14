from tkinter import *


class Interface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="Url del video")
        self.fnameLabel.grid()

        self.fnameEntry = StringVar()
        self.fnameEntry = Entry(textvariable=self.fnameEntry)
        self.fnameEntry.grid()

        def buttonClick():
            print("You pressed Submit!")
            print(self.fnameEntry.get() + ", you clicked the button!")

        self.submitButton = Button(master, text="Descargar", command=buttonClick)
        self.submitButton.grid()


# We use this as a logger for all the errors we might get downloading the video
class Logger(object):
    def debug (self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


if __name__ == "__main__":
    guiFrame = Interface()
    guiFrame.mainloop()