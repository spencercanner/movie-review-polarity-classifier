###
# This program allows the user to select a file and then display it's contents in a text widget.
# This program is a modified version from this source code: http://zetcode.com/gui/tkinter/dialogs/
###

from Tkinter import Frame, Tk, BOTH, Text, Menu, END
import tkFileDialog

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        # This is the text widget which will show the contents of a selected file.
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)




    def onOpen(self):

        # These are file filters. The first shows only Text files, the other shows all files.
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            # Read the contents of the file.
            text = self.readFile(fl)
            # The text is inserted into the Text widget.
            self.txt.insert(END, text)
            # The text is printed in the console.
            print text

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
