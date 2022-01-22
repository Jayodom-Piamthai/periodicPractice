import random
from re import A
import time
import tkinter

GroupAList = ('h','li','na','k','rb','cs','fr','be','mg','ca','sr','b','al','ga','in','tl','nh','c','si','ge','sn','pb','fl','n','p','as','sb','bi','mc','o','s','se','te','po','lv','f','cl','br','i','at','ts','he','ne','ar','kr','xe','rn','og')
a1 = ['h','li','na','k','rb','cs','fr']
a2 = ['be','mg','ca','sr','ba','ra']
a3 = ['b','al','ga','in','tl','nh']
a4 = ['c','si','ge','sn','pb','fl']
a5 = ['n','p','as','sb','bi','mc']
a6 = ['o','s','se','te','po','lv']
a7 = ['f','cl','br','i','at','ts']
a8 = ('he','ne','ar','kr','xe','rn','og') 
GroupBList = ['Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Ti','Zr','Hf','Rf','V','Nb','Ta','Db','Cr','Mo','W','Sg','Mn','Tc','Re','Bh','Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn']
b1 = ('Cu','Ag','Au','Rg')
b2 = ('Zn','Cd','Hg','Cn')
b3 = ('Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr')
b4 = ('Ti','Zr','Hf','Rf')
b5 = ('V','Nb','Ta','Db')
b6 = ('Cr','Mo','W','Sg')
b7 = ('Mn','Tc','Re','Bh')
b8 = ('Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn')

def GroupATest():
    testA=0 ; pointA=0 ; correctAnswer = 0
    while testA < 20 :
        sampled_list = random.sample(GroupAList,1)
        print(sampled_list)
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
        #print(correctAnswer)  #//value test//
        answer = input("is in:A")
        try:
            if correctAnswer == int(answer):
                print("correct")
                testA=testA + 1 ; pointA = pointA + 1
            else:
                print("incorrect")
                testA=testA + 1
        except:
            print("incorrect")
            testA=testA + 1
    print(f"your score is {pointA}")
    
def GroupBTest():
    testB=0 ; pointB=0
    while testB < 20 :
        sampled_list = random.sample(GroupBList,1)
        print(sampled_list)
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
        #print(correctAnswer)  #//value test//
        answer = input("is in:B")
        try:
            if correctAnswer == int(answer):
                print("correct")
                testB=testB + 1 ; pointB = pointB + 1
            else:
                print("incorrect")
                testB=testB + 1
        except:
            print("incorrect")
            testB=testB + 1
def PTPinitiate():
    while 1>0 :
        gameMode = input()
        if gameMode == "T1" :
            GroupATest()
        elif gameMode == "T2" :
            GroupBTest()
        else :
            print("ERROR:try again")

print("Welcome to Periodic Table Practice" )
print("How To Play:choose your prefered mode by type T1,T2,which will also start the round" )
print("T1 = Group A only test,T2 = Group B only test" )
PTPinitiate()
    
