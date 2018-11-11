# Data Set Analyser
# Using Tkinter GUI

# Importing required packages
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as msg

import pandas as pd
import matplotlib.pyplot as plt


# Making class for the GUI
class DataSetAnalyser:

    # Initializer method
    def __init__(self, root):

        self.root = root

        # Retrieving DataSet Filename if saved before
        try:

            self.datasetname = self.retrievefilename()
            self.df = pd.read_csv(self.datasetname)

        except:

            msg.showerror("Error", "No file found, please save file")

        # Setting up the GUI
        root.geometry("600x400")
        root.resizable(False, False)
        root.title("Dataset Analyser")

        # Changing options for dataset display
        pd.set_option("display.max_columns", 500)
        pd.set_option("display.width", 1000)

        # Creating a Menu Bar
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.opendataset)
        self.filemenu.add_command(label="Save", command=self.savefilename)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Creating the dataset preview Text feild
        self.prev = Text(root, width=72, height=10)
        self.prev.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.prev.config(wrap="none")

        # Adding Horizontal and Vertical Scrollbars
        self.scrolly = Scrollbar(self.root, command=self.prev.yview)
        self.scrolly.grid(row=0, column=1, sticky="nsew")
        self.prev["yscrollcommand"] = self.scrolly.set

        self.scrollx = Scrollbar(
            self.root, orient="horizontal", command=self.prev.xview)
        self.scrollx.grid(row=1, column=0, sticky="nsew")
        self.prev["xscrollcommand"] = self.scrollx.set

        self.prev.insert("1.0", self.df.head())

        self.tools = Frame(root, border=1, relief=GROOVE, background="red")
        self.tools.grid(row=2, column=0, columnspan=2,
                        sticky=E+W, padx=5, pady=5)

        self.info_dis = Button(self.tools, text="Info", command=self.show_info)
        self.info_dis.grid(row=0, column=0)

        self.desc = Button(self.tools, text="Describe", command=self.showdesc)
        self.desc.grid(row=0, column=1)

        self.head_label = Label(self.tools, text="No. of rows")
        self.head_label.grid(row=0, column=3, sticky=W)

        self.head_int = Entry(self.tools, width=2)
        self.head_int.grid(row=0, column=4)

        self.head = Button(self.tools, text="Head", command=self.showhead)
        self.head.grid(row=0, column=2)

        root.config(menu=self.menubar)

    def opendataset(self):
        self.datasetname = askopenfilename()
        # msg.showinfo("Input Data Set", "You have selected {} file as the Data Set".format(self.datasetname))
        self.readdata()

    def savefilename(self):
        with open("filename.txt", "w") as fw:
            fw.write(self.datasetname)
            msg.showinfo(
                "Success", "Successfuly saved the current dataset filename!")

    def retrievefilename(self):
        with open("filename.txt", "r") as fr:
            return fr.read()

    def readdata(self):
        self.df = pd.read_csv(self.datasetname)
        self.prev.insert("1.0", self.df.head())

    def show_info(self):
        self.prev.delete("1.0", END)
        self.prev.insert("1.0", str(self.df.info()))

    def showdesc(self):
        self.prev.delete("1.0", END)
        self.prev.insert("1.0", str(self.df.describe()))

    def showhead(self):
        self.prev.delete("1.0", END)
        try:
            self.prev.insert("1.0", str(
                self.df.head(int(self.head_int.get()))))
        except:
            pass


def Main():
    root = Tk()
    gui = DataSetAnalyser(root)
    root.mainloop()


if __name__ == "__main__":
    Main()
