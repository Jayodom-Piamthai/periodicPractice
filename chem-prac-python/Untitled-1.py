from tkinter import *
root=Tk()


def delete():
    groupAtest.grid_forget()
frame=LabelFrame(root,text="Frameeee",padx=200,pady=200)
frame.pack(padx=8,pady=8)
groupAtest=Button(frame,text ="Group A elements",command=delete(),font=(10),padx=50,pady=50,bg="red",fg="white")
groupAtest.grid(row=1,column=3)
root,mainloop()

