from tkinter import *
import random
root=Tk()
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


sampled_list = random.sample(GroupAList,1)
frameA=LabelFrame(root,text="//Group A Elements//",padx=68,pady=38)
frameA.grid(row=0,column=0,padx=5,pady=5)
question=Label(frameA,text=f"{sampled_list}",font=(20))
question.grid(row=0,columnspan=69)

mainloop()
