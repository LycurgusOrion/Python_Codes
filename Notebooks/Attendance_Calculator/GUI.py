# GUI
import tkinter as tk
from PIL import ImageTk, Image
import os
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
    
    # refresh()
    global root
    root = tk.Toplevel()

    root.geometry("1336x720")

    m = tk.PanedWindow(root, bd=4, bg="black")
    m.pack(fill=tk.X, expand=1)

    img_attendance = ImageTk.PhotoImage(Image.open("MyAttendance.png"))
    panel_one = tk.Label(m, image = img_attendance)

    img_bunks = ImageTk.PhotoImage(Image.open("MyBunks.png"))
    panel_two = tk.Label(m, image = img_bunks)

    # m_h = tk.PanedWindow(root, bd=4, bg="black")
    rf = tk.Button(root, text="Refresh", command=refresh)
    rf.pack(expand=True, fill=tk.BOTH)

    m.add(panel_one)
    m.add(panel_two)

    root.mainloop()


main = tk.Tk()
root = None

l1 = tk.Label(main, text="Username")
l2 = tk.Label(main, text="Password")

t1 = tk.Entry(main)
t2 = tk.Entry(main)

try:
    with open("creds.txt", "r+") as fi:
        l = list(map(lambda x: x.strip("\n"), fi.readlines()))
        t1.insert(0, l[0])
        t2.insert(0, l[1])
except:
    t1.insert(0, "Enter User Name")
    t2.insert(0, "Enter Password")

l1.grid(row=0, column=0, sticky=tk.E)
l2.grid(row=1, column=0, sticky=tk.E)
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)

save = tk.Button(main, text="Save", command=save_details)
save.grid(row=2, column=0, columnspan=2, sticky=tk.E+tk.W)

launch = tk.Button(main, text="Launch", command=launch_details)
launch.grid(row=3, columnspan=2, sticky=tk.E+tk.W)

ref = tk.Button(main, text="Refresh", command=refresh)
ref.grid(row=4, columnspan=2, sticky=tk.E+tk.W)

main.mainloop()