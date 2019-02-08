# GUI
from tkinter import Tk, Label, PanedWindow, Button, Entry, Toplevel, E, W, X, BOTH
from PIL.ImageTk import PhotoImage
from PIL import Image

import Attendance_Calculator as ac
import config

def refresh():
    try:
        root.destroy()
    except:
        pass
    ac.Main()
    launch_details()


def save_details():
    l = [t1.get()+"\n", t2.get()]
    with open("creds.txt", "w") as fo:
        fo.writelines(l)


def launch_details():
    
    global root
    root = Toplevel()

    root.geometry("1336x720")

    m = PanedWindow(root, bd=4, bg="black")
    m.pack(fill=X, expand=1)

    try:
        img_attendance = PhotoImage(Image.open("MyAttendance.png"))
        panel_one = Label(m, image = img_attendance)

        img_bunks = PhotoImage(Image.open("MyBunks.png"))
        panel_two = Label(m, image = img_bunks)

        img_att = PhotoImage(Image.open("AttendanceDetails.png"))
        panel_three = Label(m, image = img_att)
    
    except:
        refresh()

        img_attendance = PhotoImage(Image.open("MyAttendance.png"))
        panel_one = Label(m, image = img_attendance)

        img_bunks = PhotoImage(Image.open("MyBunks.png"))
        panel_two = Label(m, image = img_bunks)

        img_att = PhotoImage(Image.open("AttendanceDetails.png"))
        panel_three = Label(m, image = img_att)

    # m_h = tk.PanedWindow(root, bd=4, bg="black")
    rf = Button(root, text="Refresh", command=refresh)
    rf.pack(expand=True, fill=BOTH)

    m.add(panel_one)
    m.add(panel_two)
    m.add(panel_three)

    root.mainloop()


main = Tk()
root = None

l1 = Label(main, text="Username")
l2 = Label(main, text="Password")

t1 = Entry(main)
t2 = Entry(main)

try:
    with open("creds.txt", "r+") as fi:
        l = list(map(lambda x: x.strip("\n"), fi.readlines()))
        t1.insert(0, l[0])
        t2.insert(0, l[1])
except:
    t1.insert(0, "Enter User Name")
    t2.insert(0, "Enter Password")

l1.grid(row=0, column=0, sticky=E)
l2.grid(row=1, column=0, sticky=E)
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)

save = Button(main, text="Save", command=save_details)
save.grid(row=2, column=0, columnspan=2, sticky=E+W)

launch = Button(main, text="Launch", command=launch_details)
launch.grid(row=3, columnspan=2, sticky=E+W)

ref = Button(main, text="Refresh", command=refresh)
ref.grid(row=4, columnspan=2, sticky=E+W)

main.mainloop()