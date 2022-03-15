from tkinter import *

root=Tk()
root.title("Periodic Practice")
root.iconbitmap("projectAndShits(transparent).ico")

welcome= Label(root,text="welcome to periodic practice",font=("THsarabun",20))
instruction=Label(root,text="please choose the type of test you wish to take",font=("THsarabun",20))
welcome.pack()
instruction.pack()

groupAtest=Button(root,text ="Group A elements",padx=100,pady=100,bg="red",fg="white")
groupBtest=Button(root,text ="Group B elements",padx=100,pady=100,bg="blue",fg="white")
groupAtest.grid(row=2,column=0,columnspan=1)
groupBtest.grid(row=2,column=1,columnspan=2)
root.mainloop()