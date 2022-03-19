from tkinter import *
from tkinter.ttk import Labelframe
import random

#------------------///////////////////////------------------------////////////////////////---------------------------------////////////////////////////--------------------------

#Remember the day,ace,remember the 29th of june,2019,yes,DONT EVER forget it
#19/03/22-ตามตรงนะ SSHก็น่าสนนะ,เอซ
root=Tk()
root.title("Periodic Practice")
root.iconbitmap("projectAndShits(transparent).ico")

#PereodicTable           #what a hastle
GroupAList = ('H','Li','Na','K','Rb','Cs','Fr','Be','Mg','Ca','Sr','Ba','Ra','B','Al','Ga','In','Tl','Nh','C','Si','Ge','Sn','Pb','Fl','N','P','As','Sb','Bi','Mc','O','S','Se','Te','Po','Lv','F','Cl','Br','I','At','Ts','He','Ne','Ar','Kr','Xe','Rn','Og')
a1 = ['H','Li','Na','K','Rb','Cs','Fr']
a2 = ['Be','Mg','Ca','Sr','Ba','Ra']
a3 = ['B','Al','Ga','In','Tl','Nh']
a4 = ['C','Si','Ge','Sn','Pb','Fl']
a5 = ['N','P','As','Sb','Bi','Mc']
a6 = ['O','S','Se','Te','Po','Lv']
a7 = ['F','Cl','Br','I','At','Ts']
a8 = ['He','Ne','Ar','Kr','Xe','Rn','Og'] 
GroupBList = ('Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Ti','Zr','Hf','Rf','V','Nb','Ta','Db','Cr','Mo','W','Sg','Mn','Tc','Re','Bh','Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn')
b1 = ['Cu','Ag','Au','Rg']
b2 = ['Zn','Cd','Hg','Cn']
b3 = ['Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']
b4 = ['Ti','Zr','Hf','Rf']
b5 = ['V','Nb','Ta','Db']
b6 = ['Cr','Mo','W','Sg']
b7 = ['Mn','Tc','Re','Bh']
b8 = ['Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn']

#GroupATest
def initiateA():
    global test
    global point
    global correctAnswer
    global questionA
    global sampled_list
    #randomizer/limiter
    test=0 ; point=0 ; correctAnswer = 0
    transition()
    sampled_list = random.sample(GroupAList,1)
    #answerUI
    frameA=LabelFrame(root,text="//Group A Elements//",padx=100,pady=100)
    frameA.grid(row=0,column=0,padx=5,pady=5)
    questionA=Label(frameA,text=f"{sampled_list}",font=(80))
    questionA.grid(row=1,columnspan=69)
    ChoiceA=[
        ("A1",1,2,0),("A2",2,2,1),("A3",3,2,2),("A4",4,2,3),
        ("A5",5,3,0),("A6",6,3,1),("A7",7,3,2),("A8",8,3,3),
    ]
    answer= IntVar()
    answer.set("A1")
    for choiceText,answerInput,rowPos,columnPos in ChoiceA:
        Radiobutton(frameA,text=choiceText,variable=answer,value=answerInput).grid(row=rowPos,column=columnPos)
    
    #COREKTSIONAL
    correct=Label(frameA,text="Correct!",font=(20),bg="green")
    incorrect=Label(frameA,text="Incorrect!",font="20",bg="Red")
    
    #submit
    def clicked(value):
        global test
        global point
        global correctAnswer
        global questionA
        global sampled_list
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
    
        if correctAnswer == int(value):
            print("correct")
            #clean Slate
            correct.grid_forget();incorrect.grid_forget()
            #Correct!!!
            test=test+1 ;point = point + 1
            correct.grid(row=6,columnspan=69)
            correct.grid_forget
            #question Update
            questionA.grid(row=1,columnspan=69)
            sampled_list=random.sample(GroupAList,1)
            questionA.grid_forget()
            questionA=Label(frameA,text=f"{sampled_list}",font=(80))
            questionA.grid(row=1,columnspan=69)
            #stat Update
            statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
            statistic.grid(row=0,columnspan=69)

        else:
            print("incorrect")
            #clean Slate
            correct.grid_forget();incorrect.grid_forget()
            #Incorrect!!!
            test=test+1
            incorrect.grid(row=6,columnspan=69)
            #question update
            questionA.grid(row=1,columnspan=69)
            sampled_list=random.sample(GroupAList,1)
            questionA.grid_forget()
            questionA=Label(frameA,text=f"{sampled_list}",font=(80))
            questionA.grid(row=1,columnspan=69)
            #stat Update
            statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
            statistic.grid(row=0,columnspan=69)
        print(test,point)
    #Buttons
    submit=Button(frameA,text="Submit Answer",command=lambda:clicked(answer.get()))
    submit.grid(row=4,columnspan=69)
    def Exit():
        frameA.grid_forget();frame.grid(row=0,column=0,padx=5,pady=5)
    exit=Button(frameA,text="Return To Menu",command=Exit,bg="black",fg="white")
    exit.grid(row=5,columnspan=69)

    #score
    statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
    statistic.grid(row=0,columnspan=69)
        

#GroupBTest
def initiateB():
    global test
    global point
    global correctAnswer
    global questionA
    global sampled_list
    #randomizer/limiter
    test=0 ; point=0 ; correctAnswer = 0
    transition()
    sampled_list = random.sample(GroupBList,1)
    #answerUI
    frameA=LabelFrame(root,text="//Group A Elements//",padx=100,pady=100)
    frameA.grid(row=0,column=0,padx=5,pady=5)
    questionA=Label(frameA,text=f"{sampled_list}",font=(80))
    questionA.grid(row=1,columnspan=69)
    ChoiceA=[
        ("B1",1,2,0),("B2",2,2,1),("B3",3,2,2),("B4",4,2,3),
        ("B5",5,3,0),("B6",6,3,1),("B7",7,3,2),("B8",8,3,3),
    ]
    answer= IntVar()
    answer.set("A1")
    for choiceText,answerInput,rowPos,columnPos in ChoiceA:
        Radiobutton(frameA,text=choiceText,variable=answer,value=answerInput).grid(row=rowPos,column=columnPos)
    
    #COREKTSIONAL
    correct=Label(frameA,text="Correct!",font=(20),bg="green")
    incorrect=Label(frameA,text="Incorrect!",font="20",bg="Red")
    
    #submit
    def clicked(value):
        global test
        global point
        global correctAnswer
        global questionA
        global sampled_list
        if (sampled_list[0]) in b1 :
            correctAnswer = correctAnswer*0+1
        elif (sampled_list[0]) in b2 :
            correctAnswer = correctAnswer*0+2
        elif (sampled_list[0]) in b3 :
            correctAnswer = correctAnswer*0+3
        elif (sampled_list[0]) in b4 :
            correctAnswer = correctAnswer*0+4
        elif (sampled_list[0]) in b5 :
            correctAnswer = correctAnswer*0+5
        elif (sampled_list[0]) in b6 :
            correctAnswer = correctAnswer*0+6
        elif (sampled_list[0]) in b7 :
            correctAnswer = correctAnswer*0+7
        elif (sampled_list[0]) in b8 :
            correctAnswer = correctAnswer*0+8
        print(correctAnswer)  #//value test//
    
        if correctAnswer == int(value):
            print("correct")
            #clean Slate
            correct.grid_forget();incorrect.grid_forget()
            #Correct!!!
            test=test+1 ;point = point + 1
            correct.grid(row=6,columnspan=69)
            correct.grid_forget
            #question Update
            questionA.grid(row=1,columnspan=69)
            sampled_list=random.sample(GroupBList,1)
            questionA.grid_forget()
            questionA=Label(frameA,text=f"{sampled_list}",font=(80))
            questionA.grid(row=1,columnspan=69)
            #stat Update
            statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
            statistic.grid(row=0,columnspan=69)

        else:
            print("incorrect")
            #clean Slate
            correct.grid_forget();incorrect.grid_forget()
            #Incorrect!!!
            test=test+1
            incorrect.grid(row=6,columnspan=69)
            #question update
            questionA.grid(row=1,columnspan=69)
            sampled_list=random.sample(GroupBList,1)
            questionA.grid_forget()
            questionA=Label(frameA,text=f"{sampled_list}",font=(80))
            questionA.grid(row=1,columnspan=69)
            #stat Update
            statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
            statistic.grid(row=0,columnspan=69)
        print(test,point)
    #Buttons
    submit=Button(frameA,text="Submit Answer",command=lambda:clicked(answer.get()))
    submit.grid(row=4,columnspan=69)
    def Exit():
        frameA.grid_forget();frame.grid(row=0,column=0,padx=5,pady=5)
    exit=Button(frameA,text="Return To Menu",command=Exit,bg="black",fg="white")
    exit.grid(row=5,columnspan=69)

    #score
    statistic=Label(frameA,text=f"Question Done:{test} Correct:{point}",bg="blue",fg="orange")
    statistic.grid(row=0,columnspan=69)
    
#welcomepage
frame=LabelFrame(root,text="//Main Menu//",padx=68,pady=38)
welcome= Label(frame,text="//welcome to periodic practice//",font=("THsarabun",20,"bold"))
instruction=Label(frame,text="please choose the type of test you wish to take",font=("THsarabun",20))
MyWork=Label(frame,text="Made by:Ace J.P. 2019 lmaolmaolmao 	L Fudyh Frfrd")#y'know,ace,we're really fucking lazy theese days,its a shame we spend all those wasted time watching youtube and making that tower o babel...,wait,maybe the last one aint a waste o time
welcome.grid(row=0,columnspan=3)
instruction.grid(row=1,columnspan=3)
MyWork.grid(row=3,columnspan=3)
frame.grid(row=0,column=0,padx=5,pady=5)
#Buttons
groupAtest=Button(frame,text ="Group A elements",font=(10),command=initiateA,padx=50,pady=50,bg="red",fg="white")
groupBtest=Button(frame,text ="Group B elements",font=(10),command=initiateB,padx=50,pady=50,bg="blue",fg="white")
Execute=Button(frame,text="End Program",command=root.quit,padx=10,pady=5,bg="black",fg="white")
groupAtest.grid(row=2,column=0)
groupBtest.grid(row=2,column=1,columnspan=2)
Execute.grid(row=5,columnspan=3)

def transition():
    #frameForget
    frame.grid_forget()

root.mainloop()


#Ace,you've done well,well,its not as we initially planned,with all those 20-limit and shits,but HEY!,we did it,yo. nicely done,at least for now,till next time.