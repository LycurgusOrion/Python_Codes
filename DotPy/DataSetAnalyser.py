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
        pd.set_option("display.max_rows", 500)
        pd.set_option("display.width", 1000)
        # pd.set_option("display.height", 1000)

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

        # Inserting the Head of Data Frame in the Text Feild
        self.prev.insert("1.0", self.df.head())

        # Creating Options for basic Operations
        self.tools = Frame(root, border=1, relief=GROOVE)
        self.tools.grid(row=2, column=0, columnspan=2,
                        sticky=E+W, padx=10, pady=10)

        self.head_label = Label(self.tools, text="Rows")
        self.head_label.grid(row=0, column=0, sticky=W)

        self.head_int = Entry(self.tools, width=2)
        self.head_int.grid(row=0, column=1)

        self.head = Button(self.tools, text="Head", command=self.showhead)
        self.head.grid(row=0, column=2)
        
        self.desc = Button(self.tools, text="Describe", command=self.showdesc)
        self.desc.grid(row=0, column=3, columnspan=4)

        self.origin = Button(self.tools, text="Original", command=self.readdata)
        self.origin.grid(row=0, column=8)

        # Adding List of columns to select from
        self.list_of_cols = list(self.df)
        # List containing the colums to be dropped
        self.droplist = []
        # Dictionary of selected columns
        self.dic_of_cols = {key: 0 for key in self.list_of_cols}

        # Creating different frame for checkboxes
        self.chkbx = Frame(root, border=1, relief=GROOVE)
        self.chkbx.grid(row=3, column=0, columnspan=2,
                        sticky=E+W, padx=10, pady=10)

        r, c = 0, 0
        for column in self.list_of_cols:
            self.dic_of_cols[column] = Variable()
            chk = Checkbutton(self.chkbx, text=column,
                              variable=self.dic_of_cols[column])
            chk.grid(row=r, column=c)
            chk.deselect()
            c += 1
            if c is 4:
                c = 0
                r += 1

        # Adding buttons to operate the checkboxes
        self.select_cols = Button(root, text="Update", command=self.selcols)
        self.select_cols.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E+W)

        # Adding the menubar to the mainframe
        root.config(menu=self.menubar)

    def selcols(self):

        self.list_of_cols = []
        for cols in self.dic_of_cols:
            if int(self.dic_of_cols[cols].get()) == 1:
                self.list_of_cols.append(cols)
        
        self.droplist = [x for x in list(self.df) if x not in self.list_of_cols]

        self.df.drop(columns=self.droplist, inplace=True)

        self.prev.delete("1.0", END)
        self.prev.insert("1.0", self.df.head())

    def opendataset(self):

        # Opening a file using the browse functionality
        self.datasetname = askopenfilename()
        self.readdata()

    def savefilename(self):

        # Opening file in write mode to save the dataset name
        with open("filename.txt", "w") as fw:
            fw.write(self.datasetname)
            msg.showinfo(
                "Success", "Successfuly saved the current dataset filename!")

    def retrievefilename(self):

        # Opening file in read mode to get the saved filename
        with open("filename.txt", "r") as fr:
            return fr.read()

    def readdata(self):
        self.df = pd.read_csv(self.datasetname)
        self.prev.delete("1.0", END)
        self.prev.insert("1.0", self.df.head())

    def showdesc(self):
        self.prev.delete("1.0", END)
        self.prev.insert("1.0", self.df.describe())

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
