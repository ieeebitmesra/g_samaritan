#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re
def flager(intercept):
    global a
    global b
    global c
    global d
    global e
    a=0
    b=0
    c=0
    d=0
    e=0
    typeone=re.compile(r'al qaeda|iraq|taliban|abbu sayyaf group|hamas|ltte|national liberaation army|palestine liberation front|isis|lashkar-e-tayyiba|indian mujahiddin|hizbul mujahiddin|revolutionary armed forces of columbianational liberation army')
    typethree=re.compile(r'ammonium nitrate|bendiocarb|arsine|carbofuran|diazonin|chlorine|ethion|hydrogen cyanide|hydrogen peroxide|hydrogen peroxide|mercuric chloride|mehtidathion|methomyl|mevinphos|nitro methane| oxamyl|paraquet|phorate|phosgene|sodium azide|sodium chlorate|terbufos|zinc cyanide')
    typefour=re.compile(r'ak-47|kalashnikov rifle|m16 rifle|heckler and koch rifle|fn fal|rpk machine gun|dragunov sniper rifle|assault rifle|rifle|pistol|grenade|snipers|rifles')
    typetwo=re.compile(r'imad mughmiyah|hasan izz-al-din|ali arwa|mohammed atef|osama|umstafa fadil|ahmed ghailani|anas allibi')
    typefive=re.compile(r'kill|avenge|breach|security|randevouz|safe house|operative|enter')
    tcch=typefive.findall(intercept)
    ttgp=typeone.findall(intercept)
    tcml=typethree.findall(intercept)
    twpn=typefour.findall(intercept)
    tppl=typetwo.findall(intercept)
    lttgp=len(ttgp)
    ltppl=len(tppl)
    ltcml=len(tcml)
    ltwpn=len(twpn)
    ltcch=len(tcch)
    if lttgp>0:
        a=1
    if ltppl>0:
        b=1
    if ltcml>0:
        c=1
    if ltwpn>0:
        d=1
    if ltcch>0:
        e=1
#-------------------------------------------------------------------------------------------------------------------------------
def threatim():
    global threat
    threat= a*(b+c+d+e)+ b*(a+c+d+e)+ c*(a+b+d+e) +d*(a+b+c+e)+e*(a+b+c+d)
    if threat>0:
        if a==1:
            print("terror group threat")
        if b==1:
            print("personelle threat")
        if c==1:
             print("chemical threat")
        if d==1:
            print("weapon threat")
    
    print("threat level on a scale of 0 to 20:  " + str(threat))
#---------------------------------------------------------------------------------------------------------------------------------
def phonetrack(intercom):
    iranph=re.compile(r'98\d\d\d\d\d\d\d\d\d\d')
    sudanph=re.compile(r'249\d\d\d\d\d\d\d\d\d')
    syriaph=re.compile(r'963\d\d\d\d\d\d\d\d\d')
    cubaph=re.compile(r'53\d\d\d\d\d')
    libyaph=re.compile(r'218\d\d\d\d\d\d\d\d\d\d')
    syemph=re.compile(r'967\d\d\d\d\d\d\d\d\d')
    pakph=re.compile(r'92\d\d\d\d\d\d\d\d\d\d')
    afgph=re.compile(r'93\d\d\d\d\d\d\d\d\d')
    indiaph=re.compile(r'91\d\d\d\d\d\d\d\d\d\d')
    #-----------------------------------------------------------------------------------------------------------------
    iranl=iranph.findall(intercom)
    sudanl=sudanph.findall(intercom)
    syrial=syriaph.findall(intercom)
    cubal=cubaph.findall(intercom)
    libyal=libyaph.findall(intercom)
    syeml=syemph.findall(intercom)
    pakl=pakph.findall(intercom)
    afgl=afgph.findall(intercom)
    indial=indiaph.findall(intercom)
    #----------------------------------------------------------------------------------------------------------------
    lir=len(iranl)
    lsud=len(sudanl)
    lsyr=len(syrial)
    lcub=len(cubal)
    llib=len(libyal) 
    lsyem=len(syeml)
    lpak=len(pakl)
    lafg=len(afgl)
    lind=len(indial)
    #------------------------------------------------------------------------------------------------------------------------
    if (len(iranl)+len(sudanl)+len(syrial)+len(cubal)+len(libyal)+len(syeml)+len(pakl)+len(afgl)+len(indial))>0:
        print("phone numbers detected")
    #------------------------------------------------------------------------------------------------------------------------
    if lir>0:
        print("phone number from iran:  "+','.join(iranl))
    if lsud>0:
        print("phone number from sudan:  "+','.join(sudanl))
    if lsyr>0:
        print("phone number from syria:  "+','.join(syrial))
    if lcub>0:
        print("phone number from cuba:   "+','.join(cubal))
    if llib>0:
        print("phone number from libya:  "+','.join(libyal))
    if lsyem>0:
        print("phone number from south yemen:  "+','.join(syeml))
    if lpak>0:
        print("phone number from pakistan:  "+','.join(pakl))
    if lafg>0:
        print("phone number from afghanistan:  "+','.join(afgl))
    if lind>0:
        print("phone number from india:  "+','.join(indial))
def cordet(intercept1):
    cord=re.compile(r"""\d\d°\d\d'\d\d"N \d\d°\d\d'\d\d"E|\d\d°\d\d'\d\d"N \d\d°\d\d'\d\d"W|\d\d°\d\d'\d\d"S \d\d°\d\d'\d\d"E|\d\d°\d\d'\d\d"S \d\d°\d\d'\d\d"W""")
    cordl=cord.findall(intercept1)
    if(len(cordl)>0):
        print(cordl) 
    else:
        print("no coordinates detected")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
testext=input("enter the intercepted text:    ")
flager(testext)
threatim()
x1=''
if threat>0:
    x1=input("the intercepted text might contain suspicious material,you can search for the presence of any phone number or geographical coordinates   (Y/N) ")
    if(x1=='Y'):
        phonetrack(testext)
        cordet(testext)
input("press enter to close")
        




    
    


# In[ ]:




