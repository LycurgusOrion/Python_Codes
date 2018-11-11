# Data Set Analyser
# Using Tkinter GUI

# GUI Libraries
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
#############################

# Computational Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#############################

# sklearn for ML
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score
#############################


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

            msg.showerror("Error", "No file found, please chose a file now")
            self.datasetname = askopenfilename()
            self.savefilename()
            self.df = pd.read_csv(self.datasetname)

        # Setting up the GUI
        root.geometry("600x600")
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

        # Creating Menu Options for basic Operations on the Dataset
        self.optionmenu = Menu(self.menubar, tearoff=0)

        self.optionmenu.add_command(label="Head", command=self.showhead)
        self.optionmenu.add_command(label="Describe", command=self.showdesc)
        self.optionmenu.add_command(label="Original", command=self.readdata)
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Update", command=self.selcols)

        self.menubar.add_cascade(label="Options", menu=self.optionmenu)

        # Creating Menu for different types of graph plots
        self.plotmenu = Menu(self.menubar, tearoff=0)

        self.plotmenu.add_command(
            label="Box", command=lambda: self.chooseparam("Box"))
        self.plotmenu.add_command(
            label="Cat", command=lambda: self.chooseparam("Cat"))
        self.plotmenu.add_command(
            label="Pair 1", command=lambda: self.chooseparam("Pair"))
        self.plotmenu.add_command(
            label="Pair 2", command=lambda: self.chooseparam("Pair_Mod"))
        self.plotmenu.add_command(
            label="Scatter", command=lambda: self.chooseparam("Scatter"))

        self.menubar.add_cascade(label="Plots", menu=self.plotmenu)

        # Label for the underlying checkboxes
        self.labelframe = Label(root, text="ATTRIBUTES",
                                border=1, relief=GROOVE)
        self.labelframe.grid(row=2, column=0, columnspan=2,
                             sticky=E+W, padx=10, pady=10)

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

        # Adding the checkbuttons
        r, c = 0, 0
        for column in self.list_of_cols:
            self.dic_of_cols[column] = Variable()
            chk = Checkbutton(self.chkbx, text=column,
                              variable=self.dic_of_cols[column], width=15)
            chk.grid(row=r, column=c, sticky=W)
            # chk.pack(side=LEFT, anchor=W, expand=YES)
            chk.deselect()
            c += 1
            if c is 4:
                c = 0
                r += 1

        self.x_col = None
        self.y_col = None

        # Adding the menubar to the mainframe
        root.config(menu=self.menubar)

    def selcols(self):

        self.list_of_cols = []
        for cols in self.dic_of_cols:
            if int(self.dic_of_cols[cols].get()) == 1:
                self.list_of_cols.append(cols)

        self.droplist = [x for x in list(
            self.df) if x not in self.list_of_cols]

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
                self.df.head(sd.askinteger("Input", "How many rows?", parent=self.root))))
        except:
            pass

    def chooseparam(self, plt_opt):
        # Creating a sub menu to chose x and y for the plot
        subxy = Toplevel(self.root)
        subxy.title("Choose X and Y")

        labelX = Label(subxy, text="Choose X")
        labelX.grid(row=0, column=0, sticky=E)

        labelY = Label(subxy, text="Choose Y")
        labelY.grid(row=1, column=0, sticky=E)

        ll = list(self.dic_of_cols.keys())

        self.x_col = StringVar(subxy)
        self.x_col.set(ll[0])

        opt = OptionMenu(subxy, self.x_col, *ll)
        opt.grid(row=0, column=1)

        self.y_col = StringVar(subxy)
        self.y_col.set(ll[0])

        opt = OptionMenu(subxy, self.y_col, *ll)
        opt.grid(row=1, column=1)

        btn = Button(subxy, text="Plot",
                     command=lambda: self.showplot(plt_opt))
        btn.grid(row=3, column=0, columnspan=2, sticky=E+W)

    def showplot(self, plt_opt):

        if plt_opt == "Box":
            sns.boxplot(x=self.x_col.get(), y=self.y_col.get(), data=self.df)
        elif plt_opt == "Cat":
            sns.catplot(x=self.x_col.get(), y=self.y_col.get(), data=self.df)
        elif plt_opt == "Pair":
            sns.pairplot(self.df, hue=self.x_col.get())
        elif plt_opt == "Pair_Mod":
            sns.pairplot(self.df[[x for x in list(
                self.dic_of_cols.keys()) if self.dic_of_cols[x].get() is 1]], hue=self.x_col)
        elif plt_opt == "Scatter":
            sns.scatterplot(x=self.x_col.get(), y=self.y_col.get(), data=self.df)

        plt.show()


def Main():
    root = Tk()
    gui = DataSetAnalyser(root)
    root.mainloop()


if __name__ == "__main__":
    Main()
