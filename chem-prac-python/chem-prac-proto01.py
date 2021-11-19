import random
from re import A
from termios import B200, B4000000, B600
import time
import tkinter

GroupAList = ['h','li','na','k','rb','cs','fr','be','mg','ca','sr','b','al','ga','in','tl','nh','c','si','ge','sn','pb','fl','n','p','as','sb','bi','mc','o','s','se','te','po','lv','f','cl','br','i','at','ts','he','ne','ar','kr','xe','rn','og']
A1 = ['h','li','na','k','rb','cs','fr']
A2 = ['be','mg','ca','sr','ba','ra']
A3 = ['b','al','ga','in','tl','nh']
A4 = ['c','si','ge','sn','pb','fl']
A5 = ['n','p','as','sb','bi','mc']
A6 = ['o','s','se','te','po','lv']
A7 = ['f','cl','br','i','at','ts']
A8 = ['he','ne','ar','kr','xe','rn','og']
GroupBList = ['Sc','Y','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Ti','Zr','Hf','Rf','V','Nb','Ta','Db','Cr','Mo','W','Sg','Mn','Tc','Re','Bh','Fe','Ru','Os','Hs','Co','Rh','Ir','Mt','Ni','Pd','Pt','Ds','Cu','Ag','Au','Rg','Zn','Cd','Hg','Cn']
B1 =()
B2 =()
B3 =()
B4 =()
B5 =()
B6 =()
B7 =()
B8 =()

def GroupATest():
    sampled_list = random.sample(GroupAList, 20)
    print(sampled_list)
    print("ready...")
    time.sleep(10)
    print("GO!")
    time.sleep(30)
    print("TIME'S UP SUCKER!")

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
print("How To Play:choose your prefered mode by type T1,T2,T3,which will also start the round" )
print("T1 = Group A only test,T2 = Group B only test,T3 = Whole periodic Table" )
PTPinitiate()
    
