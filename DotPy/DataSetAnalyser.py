# Data Set Analyser
# Using Tkinter GUI

# GUI Libraries
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
#############################

# Computational Libraries
import numpy as np
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

        # Creating Menu Options for basic Operations on the Dataset
        self.optionmenu = Menu(self.menubar, tearoff=0)

        self.optionmenu.add_command(label="Head", command=self.showhead)
        self.optionmenu.add_command(label="Describe", command=self.showdesc)
        self.optionmenu.add_command(label="Original", command=self.readdata)
        # Update the columns to only the selected ones
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Update", command=self.selcols)
        # Convert a column to numeric Operation
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="To Numeric", command=self.contonum)
        # Select All And Deselect All Operations
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Select All", command=self.select_all)
        self.optionmenu.add_command(label="Deselect All", command=self.deselect_all)

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
        self.plotmenu.add_command(
            label="Plot", command=lambda: self.chooseparam("Plot"))
        self.plotmenu.add_command(
            label="Histogram", command=lambda: self.chooseparam("Hist"))
        self.plotmenu.add_command(
            label="Bar", command=lambda: self.chooseparam("Bar"))
        self.plotmenu.add_command(
            label="Pie", command=lambda: self.chooseparam("Pie"))
        self.plotmenu.add_command(
            label="Histogram-2D", command=lambda: self.chooseparam("Hist2D"))

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

        # Checkboxes List
        self.cbuts = []

        # Adding the checkbuttons
        r, c = 0, 0
        for column in self.list_of_cols:
            self.dic_of_cols[column] = Variable()
            chk = Checkbutton(self.chkbx, text=column,
                              variable=self.dic_of_cols[column], width=15)
            chk.grid(row=r, column=c, sticky=W)
            # chk.pack(side=LEFT, anchor=W, expand=YES)
            chk.deselect()
            self.cbuts.append(chk)
            c += 1
            if c is 4:
                c = 0
                r += 1

        # Graph Plotting axes
        self.x_col = None
        self.y_col = None
        
        # Training and Testing datasets
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.X_train_scaled = None
        self.X_val_scaled = None
        self.X_val = None
        self.y_val = None

        # ExtraTreesClassifier
        self.ert = None
        self.ert_acc_scr = None
        self.ert_conf_mat = None

        # GradientBoostingClassifier
        self.gbc = None
        self.gbc_acc_scr = None
        self.gbc_conf_mat = None

        # RandomForestClassifier
        self.rfc = None
        self.rfc_acc_scr = None
        self.rfc_conf_mat = None

        # DescisionTreeClassifier
        self.dtc = None
        self.dtc_acc_scr = None
        self.dtc_conf_mat = None

        # SupportVectorClassifier
        self.svc = None
        self.svc_acc_scr = None
        self.svc_conf_mat = None

        # SGDClassifier
        self.sgd = None
        self.sgd_accr_scr = None
        self.sgd_conf_mat = None

        # LogisticRegression
        self.lr = None
        self.lr_acc_scr = None
        self.sgd_conf_mat = None

        # KNearestNeighbours
        self.knn = None
        self.knn_acc_scr = None
        self.knn_conf_mat = None        

        # Adding the Machine Learning submenu
        self.mlmenu = Menu(self.menubar, tearoff=0)

        self.mlmenu.add_command(label="Fit Transform", command=self.fittransform)
        self.mlmenu.add_command(label="Prepare", command=self.prepare)
        self.mlmenu.add_separator()
        self.mlmenu.add_command(label="KNN", command=self.knn_model)
        self.mlmenu.add_command(label="LR", command=self.lr_model)
        self.mlmenu.add_command(label="SGD", command=self.sgd_model)
        self.mlmenu.add_command(label="SVC", command=self.svc_model)
        self.mlmenu.add_command(label="DTC", command=self.dtc_model)
        self.mlmenu.add_command(label="RFC", command=self.rfc_model)
        self.mlmenu.add_command(label="GBC", command=self.gbc_model)
        self.mlmenu.add_command(label="ERT", command=self.ert_model)

        self.menubar.add_cascade(label="Models", menu=self.mlmenu)

        # Adding the menubar to the+
        #  mainframe
        root.config(menu=self.menubar)

    def prepare(self):
        ll = []
        for x in self.dic_of_cols:
            if int(self.dic_of_cols[x].get()) is 1:
                ll.append(x)
        
        if len(ll) is not 1:
            msg.showerror("Error", "Please select only one column to prepapre for!")
        else:
            X = self.df.drop(columns=[ll[0]])
            y = self.df[ll[0]]

            strat_split = StratifiedShuffleSplit(n_splits=5, train_size=0.9, random_state=42)

            for train_index, test_index in strat_split.split(X, y):
                self.X_train, self.X_test = X.iloc[train_index], X.iloc[test_index]
                self.y_train, self.y_test = y.iloc[train_index], y.iloc[test_index]
            
            # msg.showinfo("X_train.shape", str(self.X_train.shape))
            # msg.showinfo("y_train.shape", str(self.y_train.shape))
            # msg.showinfo("X_test.shape", str(self.X_test.shape))
            # msg.showinfo("y_test.shape", str(self.y_test.shape))

            strat_split_val = StratifiedShuffleSplit(n_splits=1, train_size=0.75, random_state=42)

            for train_index, val_index in strat_split_val.split(self.X_train, self.y_train):
                self.X_train, self.X_val = self.X_train.iloc[train_index], self.X_train.iloc[val_index]
                self.y_train, self.y_val = self.y_train.iloc[train_index], self.y_train.iloc[val_index]

            scaler = StandardScaler()
            self.X_train_scaled = pd.DataFrame(scaler.fit_transform(self.X_train), columns=self.X_train.columns)
            self.X_val_scaled = pd.DataFrame(scaler.transform(self.X_val), columns=self.X_val.columns)

            msg.showinfo("Success", "Successfuly prepared the test and train datasets!")

    def knn_model(self):
        self.knn = KNeighborsClassifier(n_jobs=-1)
        self.knn.fit(self.X_train_scaled, self.y_train)

        self.knn_acc_scr = str(accuracy_score(self.y_val, self.knn.predict(self.X_val_scaled)))
        self.knn_conf_mat = str(confusion_matrix(self.y_val, self.knn.predict(self.X_val_scaled)))

        knn_sub = Toplevel(self.root)
        knn_sub.title("KNN")
        knn_sub.geometry("270x120")
        
        lbl_one = Label(knn_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(knn_sub, text=self.knn_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(knn_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(knn_sub, width=20, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.knn_conf_mat)

    def lr_model(self):
        self.lr = LogisticRegression(n_jobs=-1)
        self.lr.fit(self.X_train, self.y_train)

        self.lr_acc_scr = str(accuracy_score(self.y_val, self.lr.predict(self.X_val)))
        self.lr_conf_mat = str(confusion_matrix(self.y_val, self.lr.predict(self.X_val)))

        lr_sub = Toplevel(self.root)
        lr_sub.title("LR")
        lr_sub.geometry("270x120")
        
        lbl_one = Label(lr_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(lr_sub, text=self.lr_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(lr_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(lr_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.lr_conf_mat)
    
    def sgd_model(self):
        self.sgd = SGDClassifier(n_jobs=-1)
        self.sgd.fit(self.X_train, self.y_train)

        self.sgd_acc_scr = str(accuracy_score(self.y_val, self.sgd.predict(self.X_val_scaled)))
        self.sgd_conf_mat = str(confusion_matrix(self.y_val, self.sgd.predict(self.X_val_scaled)))

        sgd_sub = Toplevel(self.root)
        sgd_sub.title("SGD")
        sgd_sub.geometry("270x120")
        
        lbl_one = Label(sgd_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(sgd_sub, text=self.sgd_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(sgd_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(sgd_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.sgd_conf_mat)

    def svc_model(self):
        self.svc = SVC()
        self.svc.fit(self.X_train, self.y_train)

        self.svc_acc_scr = str(accuracy_score(self.y_val, self.svc.predict(self.X_val_scaled)))
        self.svc_conf_mat = str(confusion_matrix(self.y_val, self.svc.predict(self.X_val_scaled)))

        svc_sub = Toplevel(self.root)
        svc_sub.title("SVC")
        svc_sub.geometry("270x120")
        
        lbl_one = Label(svc_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(svc_sub, text=self.svc_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(svc_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(svc_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.svc_conf_mat)

    def dtc_model(self):
        self.dtc = DecisionTreeClassifier()
        self.dtc.fit(self.X_train, self.y_train)

        self.dtc_acc_scr = str(accuracy_score(self.y_val, self.dtc.predict(self.X_val)))
        self.dtc_conf_mat = str(confusion_matrix(self.y_val, self.dtc.predict(self.X_val)))

        dtc_sub = Toplevel(self.root)
        dtc_sub.title("DTC")
        dtc_sub.geometry("270x120")
        
        lbl_one = Label(dtc_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(dtc_sub, text=self.dtc_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(dtc_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(dtc_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.dtc_conf_mat)

    def rfc_model(self):
        self.rfc = RandomForestClassifier(n_jobs=-1, oob_score=True)
        self.rfc.fit(self.X_train, self.y_train)

        self.rfc_acc_scr = str(accuracy_score(self.y_val, self.rfc.predict(self.X_val)))
        self.rfc_conf_mat = str(confusion_matrix(self.y_val, self.rfc.predict(self.X_val)))

        rfc_sub = Toplevel(self.root)
        rfc_sub.title("RFC")
        rfc_sub.geometry("270x120")
        
        lbl_one = Label(rfc_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(rfc_sub, text=self.rfc_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(rfc_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(rfc_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.rfc_conf_mat)

    def gbc_model(self):
        self.gbc = GradientBoostingClassifier()
        self.gbc.fit(self.X_train, self.y_train)

        self.gbc_acc_scr = str(accuracy_score(self.y_val, self.gbc.predict(self.X_val)))
        self.gbc_conf_mat = str(confusion_matrix(self.y_val, self.gbc.predict(self.X_val)))

        gbc_sub = Toplevel(self.root)
        gbc_sub.title("GBC")
        gbc_sub.geometry("270x120")
        
        lbl_one = Label(gbc_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(gbc_sub, text=self.gbc_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(gbc_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(gbc_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.gbc_conf_mat)

    def ert_model(self):
        self.ert = ExtraTreesClassifier(n_jobs=-1, oob_score=True, bootstrap=True)
        self.ert.fit(self.X_train, self.y_train)

        self.ert_acc_scr = str(accuracy_score(self.y_val, self.ert.predict(self.X_val)))
        self.ert_conf_mat = str(confusion_matrix(self.y_val, self.ert.predict(self.X_val)))

        ert_sub = Toplevel(self.root)
        ert_sub.title("ERT")
        ert_sub.geometry("270x120")
        
        lbl_one = Label(ert_sub, text="Accuracy Score")
        lbl_one.grid(row=0, column=0, sticky=E)

        lbl_two = Label(ert_sub, text=self.ert_acc_scr)
        lbl_two.grid(row=0, column=1)

        lbl_three = Label(ert_sub, text="Confusion Matrix")
        lbl_three.grid(row=1, column=0, sticky=E)

        txt = Text(ert_sub, width=10, height=5)
        txt.grid(row=1, column=1)
        txt.insert("1.0", self.ert_conf_mat)

    def select_all(self):
        for i in self.cbuts:
            i.select()
    
    def deselect_all(self):
        for i in self.cbuts:
            i.deselect()
    
    def contonum(self):
        ll = []
        for x in self.dic_of_cols:
            if int(self.dic_of_cols[x].get()) is 1:
                ll.append(x)
        
        for x in ll:
            self.df[x] = self.df[x].replace(r'\s+', np.nan, regex=True)
            self.df[x] = self.df[x].fillna(0)
            self.df[x] = pd.to_numeric(self.df[x])
        
        msg.showinfo("Success", "Successfuly Converted to Numeric!")

    def fittransform(self):
        lbl_enc = LabelEncoder()
        
        ll = []
        for x in self.dic_of_cols:
            if int(self.dic_of_cols[x].get()) is 1:
                ll.append(x)
        
        if len(ll) is not 1:
            msg.showerror("Error", "Please select only one column to transform!")
        else:
            self.df[ll[0]] = lbl_enc.fit_transform(self.df[ll[0]])
            self.showhead(1)

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

    def showhead(self, flag=0):
        self.prev.delete("1.0", END)
        if flag == 0:
            try:
                self.prev.insert("1.0", str(
                    self.df.head(sd.askinteger("Input", "How many rows?", parent=self.root))))
            except:
                pass
        else:
            self.prev.insert("1.0", self.df.head())

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
            ll = []
            for x in self.dic_of_cols:
                if int(self.dic_of_cols[x].get()) is 1:
                    ll.append(x)
            sns.pairplot(self.df[ll], hue=self.x_col.get())
        elif plt_opt == "Scatter":
            sns.scatterplot(x=self.x_col.get(), y=self.y_col.get(), data=self.df)
        elif plt_opt == "Plot":
            plt.plot(x=self.x_col.get(), y=self.y_col.get(), data=self.df)
        elif plt_opt == "Hist":
            plt.hist(x=self.x_col.get(), data=self.df)
        elif plt_opt == "Bar":
            plt.bar(x=self.x_col.get(), height=self.y_col.get(), data=self.df)
        elif plt_opt == "Pie":
            plt.pie(x=self.x_col.get(), data=self.df)
        elif plt_opt == "Hist2D":
            plt.hist2d(x=self.x_col.get(), y=self.y_col.get(), data=self.df)

        plt.show()


def Main():
    root = Tk()
    gui = DataSetAnalyser(root)
    root.mainloop()


if __name__ == "__main__":
    Main()
