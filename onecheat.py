print('OneCheat')
from tkinter import Tk, StringVar, Frame, N, W, E, S, Button, Label, Entry
from tkinter.ttk import Combobox
from requests import get
import os.path
import os
'''
Revision List:
Rev1.0:
- First Release
- New Super Mario Bros. 2 Added

Rev1.1:
- New Super Mario Bros. 2 Gold Edition
- Super Smash Bros. for 3DS
- Still no NTSC-J, or PAL support
Rev1.3:
- AR DSi Support (Stub)
- Riivolution Support (Stub)
- CTGP-R My Stuff Support
- Mario Kart Wii (Soon through Riivolution)
- Music Park
- First public release
Rev1.4:
- Future Release
- Miiverse Revival Installer
- Unstub AR DSi
- Unstub Riivolution
- Mario Kart Wii (through Riivolution)
'''
ctglocs = {'Music Park': 'rainbow_course.szs'}
ctglinks = {'Music Park': 'http://avsys.xyz/files/CTs/3DS%20Music%20Park/v2.0/rainbow_course.szs'}
links = {'New Super Mario Bros. 2':'https://github.com/FlagBrew/Sharkive/raw/master/3ds/000400000007AE00.txt','New Super Mario Bros. 2 Gold Edition':'https://github.com/FlagBrew/Sharkive/raw/master/3ds/0004000000137E00.txt','Super Smash Bros. for 3DS':'https://github.com/FlagBrew/Sharkive/raw/master/3ds/00040000000EDF00.txt'}
tids = {'New Super Mario Bros. 2':'000400000007AE00','New Super Mario Bros. 2 Gold Edition':'0004000000137E00','Super Smash Bros. for 3DS':'00040000000EDF00'}
def ds3download(lumaloc):
    if gamevar.get() == 'Miiverse':
        # Perform special steps to install rverse
        if not os.path.exists(lumaloc + 'luma'):
            print('Luma3DS is not installed to this directory!')
            exit()
    
        if not os.path.exists(lumaloc + 'luma/titles'):
            os.mkdir(lumaloc + 'luma/titles')
        if not os.path.exists(lumaloc + 'luma/titles/' + '000400300000BD02'):
            os.mkdir(lumaloc + 'luma/titles/' + '000400300000BD02')
        a = get('https://github.com/zurgeg/onecheat-rverse/raw/master/code.ips')
        f = open(lumaloc + 'luma/titles/' + '000400300000BD02/code.ips','wb')
        f.write(a.content)
        f.close()
        b = get('https://github.com/zurgeg/onecheat-rverse/raw/master/rev.pem')
        f = open(lumaloc + '3ds/rev.pem','wb')
        f.write(b.content)
        f.close()
        print('Cheat Downloaded!')
    else:
        
        a = get(links[gamevar.get()])
        downloadloc = lumaloc + 'luma/titles/' + tids[gamevar.get()] + '/cheats.txt'
        if not os.path.exists(lumaloc + 'luma'):
            print('Luma3DS is not installed to this directory!')
            exit()
        
        if not os.path.exists(lumaloc + 'luma/titles'):
            os.mkdir(lumaloc + 'luma/titles')
        if not os.path.exists(lumaloc + 'luma/titles/' + tids[gamevar.get()]):
            os.mkdir(lumaloc + 'luma/titles/' + tids[gamevar.get()])
        #print(a.content)
        f = open(downloadloc,'wb')
        f.write(a.content)
        f.close()
        print('Cheat Downloaded!')
def dsidownload(twlmloc):
    # Stub
    ...
def riidownload(riiloc):
    # Stub
    ...
def ctgdownload(ctgploc):
    a = get(ctglinks[gamevar.get()])
    if not os.path.exists(ctgploc + 'ctgpr/My Stuff'):
        print('CTGP-R not installed to this directory!')
    else:
        f = open(ctgploc + 'ctgpr/My Stuff/' + ctglocs[gamevar.get()],'wb')
        f.write(a.content)
        f.close()
        print('Cheat Downloaded!')
    
    
    
    
    
    
def choosegame():
    global gamevar
    
    ds3choices = ['New Super Mario Bros. 2','New Super Mario Bros. 2 Gold Edition','Super Smash Bros. for 3DS','Miiverse']
    dsichoices = ['None right now']
    riichoices = ['None right now']
    mschoices = ['Music Park']
    if consolevar.get() == '3DS':
        gamechoices = ds3choices
        gamevar.set('New Super Mario Bros. 2')
        gamedropdown = Combobox(rootframe, width=50, textvariable=gamevar, values=gamechoices)
        gamedropdown.grid(column = 0, row = 3)
        ok3 = Button(rootframe, text='Download!', command = lambda: ds3download(sdcardloc.get()))
        ok3.grid(column = 0, row = 7)
    elif consolevar.get() == 'DSi (AR)':
        gamechoices = dsichoices
        gamevar.set('None right now')
        gamedropdown = Combobox(rootframe, width=50, textvariable=gamevar, values=gamechoices)
        gamedropdown.grid(column = 0, row = 3)
    elif consolevar.get() == 'CTGP-R':
        gamechoices = mschoices
        gamevar.set('Music Park')
        gamedropdown = Combobox(rootframe, width=50, textvariable=gamevar, values=gamechoices)
        gamedropdown.grid(column = 0, row = 3)
        ok3 = Button(rootframe, text='Download!', command = lambda: ctgdownload(sdcardloc.get()))  
        ok3.grid(column = 0, row = 7)
    else:
        gamechoices = riichoices
        gamevar.set('None right now')
        gamedropdown = Combobox(rootframe, width=50, textvariable=gamevar, values=gamechoices)
        gamedropdown.grid(column = 0, row = 3)
    sdcardlabel = Label(rootframe,text='SD Card Location')
    sdcardloc = Entry()
    sdcardlabel.grid(column = 0, row = 4)
    sdcardloc.grid(column = 0, row = 5)
    
    

        
root = Tk()
root.title('OneCheat Installer')

rootframe = Frame(root)
rootframe.grid(column = 0,row = 0,sticky = (N,W,E,S))

consolevar = StringVar(root)
choices = ['DSi (AR)','3DS','Wii (Riivolution)','CTGP-R']
consolevar.set('3DS')

dropdown = Combobox(rootframe, width=50, textvariable=consolevar, values=choices)
dropdown.grid(column = 0, row = 1)

ok = Button(rootframe,text='Next',command=choosegame)
ok.grid(column = 0, row = 2)

gamevar = StringVar(root)

    
        



root.mainloop()
