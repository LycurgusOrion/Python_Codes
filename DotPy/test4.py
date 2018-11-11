from tkinter import *
root = Tk()

f1=Frame(root,bd=5,relief='raise')
f1.pack(side=LEFT)
f2=Frame(root,bd=5, relief='raise')
f2.pack(side=RIGHT)
f3=Frame(root,bd=5,relief='raise')
f3.pack(side=BOTTOM)
v=IntVar()
var1=IntVar()
Radiobutton(f1, text="male", variable=var1,value=1).pack(anchor=W)
Radiobutton(f1, text="female", variable=var1,value=2).pack(anchor=W)

Radiobutton(f2,text="Python",variable=v,value=1).pack(anchor=W)
Radiobutton(f2,text="PHP",variable=v,value=2).pack(anchor=W)
Radiobutton(f2,text="Java",variable=v,value=3).pack(anchor=W)
Radiobutton(f2,text="C++",variable=v,value=4).pack(anchor=W)

Button(f3, text='Quit').pack(side=BOTTOM)
Button(f3, text='Show').pack(side=BOTTOM)

mainloop()
