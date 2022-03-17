from tkinter import *
#Remember the day,ace,remember the 29th of june,2019,yes,DONT EVER forget it
root=Tk()
root.title("Periodic Practice")
root.iconbitmap("projectAndShits(transparent).ico")


frame=LabelFrame(root,text="//Main Menu//",padx=68,pady=38)
frame.grid(row=0,column=0,padx=5,pady=5)

#GroupATest
def initiateA():
    return
#GroupBTest
def initiateB():
    return
    
#welcomepage
welcome= Label(frame,text="//welcome to periodic practice//",font=("THsarabun",20,"bold"))
instruction=Label(frame,text="please choose the type of test you wish to take",font=("THsarabun",20))
MyWork=Label(frame,text="Made by:Ace J.P. 2019 lmaolmaolmao 	L Fudyh Frfrd")#y'know,ace,we're really fucking lazy theese days,its a shame we spend all those wasted time watching youtube and making that tower o babel...,wait,maybe the last one aint a waste o time
welcome.grid(row=0,columnspan=3)
instruction.grid(row=1,columnspan=3)
MyWork.grid(row=3,columnspan=3)

groupAtest=Button(frame,text ="Group A elements",font=(10),command=initiateA,padx=50,pady=50,bg="red",fg="white")
groupBtest=Button(frame,text ="Group B elements",font=(10),command=initiateB,padx=50,pady=50,bg="blue",fg="white")
groupAtest.grid(row=2,column=0)
groupBtest.grid(row=2,column=1,columnspan=2)
#endoyo
Execute=Button(frame,text="End Program",command=root.quit,padx=10,pady=5,bg="black",fg="white")
Execute.grid(row=5,columnspan=3)

root.mainloop()