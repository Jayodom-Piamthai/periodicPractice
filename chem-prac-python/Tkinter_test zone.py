from tkinter import *
from tkinter.ttk import Labelframe
import random
import time



#Remember the day,ace,remember the 29th of june,2019,yes,DONT EVER forget it
root=Tk()
root.title("Periodic Practice")
root.iconbitmap("projectAndShits(transparent).ico")


frame=LabelFrame(root,text="//Main Menu//",padx=68,pady=38)
frame.grid(row=0,column=0,padx=5,pady=5)

#PereodicTable           #what a hastle
GroupAList = ('h','li','na','k','rb','cs','fr','be','mg','ca','sr','b','al','ga','in','tl','nh','c','si','ge','sn','pb','fl','n','p','as','sb','bi','mc','o','s','se','te','po','lv','f','cl','br','i','at','ts','he','ne','ar','kr','xe','rn','og')
a1 = ['h','li','na','k','rb','cs','fr']
a2 = ['be','mg','ca','sr','ba','ra']
a3 = ['b','al','ga','in','tl','nh']
a4 = ['c','si','ge','sn','pb','fl']
a5 = ['n','p','as','sb','bi','mc']
a6 = ['o','s','se','te','po','lv']
a7 = ['f','cl','br','i','at','ts']
a8 = ['he','ne','ar','kr','xe','rn','og'] 
GroupBList = ('Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Ti','Zr','Hf','Rf','V','Nb','Ta','Db','Cr','Mo','W','Sg','Mn','Tc','Re','Bh','Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn')
b1 = ['Cu','Ag','Au','Rg']
b2 = ['Zn','Cd','Hg','Cn']
b3 = ['Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']
b4 = ['Ti','Zr','Hf','Rf']
b5 = ['V','Nb','Ta','Db']
b6 = ['Cr','Mo','W','Sg']
b7 = ['Mn','Tc','Re','Bh']
b8 = ['Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn']
IncorrectAnswer = list( )


#GroupATest
def initiateA():
    transition()

    #randomizer/limiter
    testA=0 ; pointA=0 ; correctAnswer = 0
    while testA < 20 :
        sampled_list = random.sample(GroupAList,1)

        #answerUI
        frameA=LabelFrame(root,text="//Group A Elements//",padx=100,pady=100)
        frameA.grid(row=0,column=0,padx=5,pady=5)
        question=Label(frameA,text=f"{sampled_list}",font=(80))
        question.grid(row=1,columnspan=69)
        ChoiceA=[
            ("A1",1,2,0),("A2",2,2,1),("A3",3,2,2),("A4",4,2,3),
            ("A5",5,3,0),("A6",6,3,1),("A7",7,3,2),("A8",8,3,3),
        ]
        answer= IntVar()
        answer.get()
        for choiceText,answerInput,rowPos,columnPos in ChoiceA:
            Radiobutton(frameA,text=choiceText,variable=answer,value=answerInput).grid(row=rowPos,column=columnPos)

        ConfirmedAnswer=0
        if (sampled_list[0]) in a1 :
            correctAnswer = correctAnswer*0+1
        elif (sampled_list[0]) in a2 :
            correctAnswer = correctAnswer*0+2
        elif (sampled_list[0]) in a3 :
            correctAnswer = correctAnswer*0+3
        elif (sampled_list[0]) in a4 :
            correctAnswer = correctAnswer*0+4
        elif (sampled_list[0]) in a5 :
            correctAnswer = correctAnswer*0+5
        elif (sampled_list[0]) in a6 :
            correctAnswer = correctAnswer*0+6
        elif (sampled_list[0]) in a7 :
            correctAnswer = correctAnswer*0+7
        elif (sampled_list[0]) in a8 :
            correctAnswer = correctAnswer*0+8
        print(correctAnswer)  #//value test//
        
        
        answer==ConfirmedAnswer
        try:
            if correctAnswer == int(ConfirmedAnswer):
                print("correct")
                testA=testA + 1 ; pointA = pointA + 1
            else:
                print("incorrect")
                testA=testA + 1
                IncorrectAnswer.append(f"{sampled_list}(A{correctAnswer})" )
        except:
            print("incorrect")
            testA=testA + 1
            IncorrectAnswer.append(f"{sampled_list}(A{correctAnswer})" )
        #submit
        submit=Button(frameA,text="Submit Answer")
        submit.grid(row=4,columnspan=69)

#GroupBTest
def initiateB():
    transition()
    
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

def transition():
    #frameForget
    frame.grid_forget()
    #MenuDelete
    welcome.grid_forget();instruction.grid_forget();MyWork.grid_forget();groupAtest.grid_forget();groupBtest.grid_forget();Execute.grid_forget() 

root.mainloop()