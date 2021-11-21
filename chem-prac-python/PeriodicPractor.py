import random
from re import A
import time
import tkinter

GroupAList = ['h','li','na','k','rb','cs','fr','be','mg','ca','sr','b','al','ga','in','tl','nh','c','si','ge','sn','pb','fl','n','p','as','sb','bi','mc','o','s','se','te','po','lv','f','cl','br','i','at','ts','he','ne','ar','kr','xe','rn','og']
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
    testA=0 ; pointA=0
    while testA < 20 :
        sampled_list = random.sample(GroupAList,1)
        print(sampled_list)
        input("is in:")
        if sampled_list in list(input) :
            print("correct")
            testA=testA + 1 ; pointA = pointA + 1
        else:
            print("incorrect")
            testA=testA + 1
    print(f"your score is {pointA}")
    

def GroupBTest():
    sampled_list = random.sample(GroupBList, 20)
    print(sampled_list)
    print("ready...")
    time.sleep(10)
    print("GO!")
    time.sleep(30)
    print("TIME'S UP SUCKER!")

def PTPinitiate():
    gameMode = input()
    if gameMode == "T1" :
        GroupATest()
    elif gameMode == "T2" :
        GroupBTest()
    else :
        print("ERROR:try again")
        PTPinitiate()

print("Welcome to Periodic Table Practice" )
print("How To Play:choose your prefered mode by type T1,T2,which will also start the round" )
print("T1 = Group A only test,T2 = Group B only test" )
PTPinitiate()
    
