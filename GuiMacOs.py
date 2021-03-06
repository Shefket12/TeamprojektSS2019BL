# !/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from Crawler.Crawlerpy import *
from Data.TeamIdentification import *
from tkinter import*
from Algorithm.AlgorithmInterface import *
from PIL import ImageTk, Image
import datetime
import os

#Methods for Buttons---------------------


def Crawler():
    
    BLCrawler.getSeasons(2012,2018)
    InfoVar.set("Konfigurieren Sie ihre Berechnung in den Einstellungen")
    
       
def AlgorithmConfiguration():
    
    InfoVar.set("Konfigurieren Sie die Berechnung und drücken die auf 'Bestätigen'")
    global AlgorithmConfigPopUp
    AlgorithmConfigPopUp = Toplevel()
    AlgorithmConfigPopUp.wm_title("Einstellungen")
    AlgorithmConfigPopUp.geometry(str(popUpWidth)+"x"+str(popUpHeight))
    AlgorithmConfigPopUp.grid_rowconfigure(10, minsize=100)
    AlgorithmConfigPopUp.resizable(width = False, height = False)
    
    
    firstSeason = StringVar()
    lastSeason = StringVar()
    firstGameDay = StringVar()
    lastGameDay = StringVar()
    
    #Configuration Algorithm:---------------------------------------------------------
    variableAlgorithm.set("Algorithmus Auswahl")
    dropdownAlgorithm = OptionMenu(AlgorithmConfigPopUp, variableAlgorithm, "Basis Algorithmus", "Poisson Regression")
    dropdownAlgorithm.grid(row=0,column = 0,columnspan = 4,sticky=W)
    
    #Configuration Season:------------------------------------------------------------
    Label(AlgorithmConfigPopUp, text="Saison:").grid(row=1, column = 0, sticky=W)
    
    #Entry First Season
    entryFirstSeason = Entry(AlgorithmConfigPopUp, width = 6, textvariable= firstSeason)
    entryFirstSeason.grid(row=1, column = 1, sticky=W)
    entryFirstSeason.insert(0, "2009")
    
    Label(AlgorithmConfigPopUp, text="bis").grid(row=1, column = 2, sticky=W)
    
    #Entry Last Season
    entryLastSeason = Entry(AlgorithmConfigPopUp, width = 6, textvariable= lastSeason)
    entryLastSeason.grid(row=1, column = 3, sticky=W)
    entryLastSeason.insert(0, "2018")
    
    #Configuration  GameDays:------------------------------------------------------------
    Label(AlgorithmConfigPopUp, text="Spieltage:").grid(row=2, column = 0, sticky=W)
    
    #Entry First GameDay
    entryFirstGameDay= Entry(AlgorithmConfigPopUp, width = 6, textvariable= firstGameDay)
    entryFirstGameDay.grid(row=2, column = 1, sticky=W)
    entryFirstGameDay.insert(0, "1")
    
    Label(AlgorithmConfigPopUp, text="bis").grid(row=2, column = 2, sticky=W)
    
    #Entry Last GameDay
    entryLastGameDay = Entry(AlgorithmConfigPopUp, width = 6, textvariable= lastGameDay)
    entryLastGameDay.grid(row=2, column = 3, sticky=W)
    entryLastGameDay.insert(0, "34")
   

    #Button: Algorithm Training-----------------------------------------------------------
    buttonRunTraining = Button(AlgorithmConfigPopUp, text= "Bestätigen",
                               command = combine_funcs(lambda:RunAlgorithmTraining(
                                   int(firstSeason.get()),
                                   int(lastSeason.get()),
                                   int(firstGameDay.get()),
                                   int(lastGameDay.get()),
                                   str(variableAlgorithm.get())), AlgorithmConfigPopUp.destroy))
    buttonRunTraining.grid(row=4 ,column= 0)
    

        
    #Button: Close Configuration----------------------------------------------------------
    
    
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
    
def RunAlgorithmTraining(FirstSeason, LastSeason, FirstGameDay, LastGameDay, AlgorithmChoice):
    CalcAlgo.deleteData()
    AlgorithmConfigPopUp.destroy
    
    #Basis Algorithm:
    if(AlgorithmChoice == "Basis Algorithmus"):
        CalcAlgo.setAlgorithm(0)
        InfoVar.set("Wählen Sie die Mannschaften für die Berechnung aus")
    elif((AlgorithmChoice == "Poisson Regression")):
        CalcAlgo.setAlgorithm(1)
        InfoVar.set("Wählen Sie die Mannschaften für die Berechnung aus")
    else:
        InfoVar.set("Achtung! Sie haben keinen Algorithmus ausgewählt.")
    
    CalcAlgo.setSeasons(FirstSeason, LastSeason, FirstGameDay, LastGameDay)
    CalcAlgo.processData(CVS_Path)
    NextGameDaySetUp()
    
def Calculate():
    
    if (CalcAlgo.hasMatches()):
        if(CalcAlgo.algorithmIndex != -1):
            if (str(variableHome.get()) != "Heim") and (str(variableGuest.get()) != "Gast"):
                if(str(variableHome.get())!= str(variableGuest.get())):
                    
                    
                    result = CalcAlgo.getResult(str(variableHome.get()), str(variableGuest.get()), CVS_Path)
                    imgHomeTeam.config(image = "")
                    loadHomeTeam = Image.open(f"Data/Logos/{str(variableHome.get())}.gif")
                    renderHomeTeam = ImageTk.PhotoImage(loadHomeTeam)
                    imgHomeTeam.config(image=renderHomeTeam)
                    imgHomeTeam.image = renderHomeTeam
                    imgHomeTeam.place(x=100, y=rootHeight/3)
                    
                    ResultVarHome.set(str(variableHome.get())+":\n"+ str(result[0]*100)+" %")
                    
                    imgGuestTeam.config(image = "")
                    loadGuestTeam = Image.open(f"Data/Logos/{str(variableGuest.get())}.gif")
                    renderGuestTeam = ImageTk.PhotoImage(loadGuestTeam)
                    imgGuestTeam.config(image=renderGuestTeam)
                    imgGuestTeam.image = renderGuestTeam
                    imgGuestTeam.place(x=370, y=rootHeight/3)
                    
                    ResultVarGuest.set(str(variableGuest.get())+":\n"+ str(result[1]*100)+" %")
                    
                    
                    ResultVarDraw.set("Unentschieden:\n"+ str(result[2]*100)+" %")
        
                    print("Test: "+str(result[0]+result[1]+result[2]))
        
                    #Delete InfoText
                    InfoVar.set("")
                    
                else:
                    InfoVar.set("Wählen Sie zwei unterschiedliche Mannschaften aus!")
            else:
                InfoVar.set("Wählen Sie zwei Mannschaften aus!")
        else:
            InfoVar.set("Sie haben keinen Algorithmus ausgewählt. Gehen Sie auf 'Einstellungen' und treffen Sie ein Auswahl")
    else:
        InfoVar.set("Es gibt keine Daten für die Berechnung! Starten Sie den Crawler und konfigurieren Sie die Daten in den Einstellungen.")

        
def getNextGameDay():
    
    file = "Data/nextSeason.csv"
    NSCrawler = DataCrawler(file)
    NSCrawler.getNextSeason(2019)
    result = []
    gameday = 1
    now = datetime.datetime.now().isoformat()
    #now = "2019-07-11T09:13:32.007347"
    #open the csv file
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file ,delimiter=',')
        #Skipps the first row
        next(csv_reader, None)
        #iterate over each line
        for row in csv_reader:
            
            if(gameday < int(row[2])):
                break
            
            if(gameday > int(row[2])):
                continue
            
            if(now > str(row[0])):
                gameday += 1
                continue
            
            home_team = int(row[3])
            external_team = int(row[4])
            match = [home_team, external_team]
            
            result.append(match)
    return result        
        
        
        
def NextGameDaySetUp():
    gameday = getNextGameDay()
    overall = ""
    if(CalcAlgo.algorithmIndex != -1):
        
        for game in gameday:
            
            overall = overall + get_TeamName(game[0])+" : "+get_TeamName(game[1])+"\n"
            result = CalcAlgo.getResult(get_TeamName(game[0]), get_TeamName(game[1]), CVS_Path)
            home = str("{0:.2f}".format(result[0]*100.0))+"%"
            guest = str("{0:.2f}".format(result[1]*100.0))+"%"
            overall = overall +home+" : "+guest+"\n"
            overall = overall +"\n"
            
    else:
        for game in gameday:
            overall = overall + get_TeamName(game[0])+" : "+get_TeamName(game[1])+"\n"
            overall = overall +"\n\n"
            
    NextGameDayVar.set(overall)
    
    return
    
    
#Initialize Root-Window---------------------     
root = Tk()
root.title("Softwareprojekt Bundesliga")

loadimg = Image.open("Data/Logos/Bundesliga.gif")
img = ImageTk.PhotoImage(loadimg)
root.call('wm','iconphoto', root._w, img)


#Numbers for Root and Widgets---------------------
rootWidth = 800
rootHeight = 450
rootResulution = str(rootWidth)+"x"+str(rootHeight)
root.geometry(rootResulution)
root.resizable(width = False, height = False)

popUpHeight = 105
popUpWidth = 250

buttonHeight = 40
buttonWidth = rootWidth/3

dropdownHeight = 30
dropdownWidth = rootWidth/3

#Initialize variables for calculation

CVS_Path = "Data/BundesligaData.csv" 

CalcAlgo = AlgorithmInterface()
BLCrawler = DataCrawler(CVS_Path)

imgHomeTeam = Label(root)
imgGuestTeam = Label(root)


# Initialize Widgets---------------------

#Buttons
buttonCrawler = Button(root, text = "Crawler", command = Crawler)
buttonAlgorithm = Button(root, text = "Einstellungen", command = AlgorithmConfiguration)
buttonCalculate = Button(root, text = "Berechnung", command = Calculate)

#DropDownMenu
variableHome = StringVar(root)
variableGuest = StringVar(root)
variableAlgorithm = StringVar(root)
variableHome.set("Heim") 
variableGuest.set("Gast") 

dropdownHome = OptionMenu(root, variableHome, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "FC Schalke 04", "VfL Wolfsburg","1. FC Köln", "SC Paderborn 07","1. FC Union Berlin")
dropdownGuest = OptionMenu(root, variableGuest,"FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "FC Schalke 04", "VfL Wolfsburg","1. FC Köln", "SC Paderborn 07","1. FC Union Berlin")

#Text
InfoVar = StringVar()
InfoVar.set("Starten Sie den Crawler")
InfoText = Message(root,textvariable = InfoVar, width= rootWidth, relief = "flat", fg = "red", bg = "white")

ResultVarHome = StringVar()
ResultVarHome.set("")
ResultTextHome = Message(root,textvariable = ResultVarHome, width= rootWidth, relief = "flat", bg = "white")

ResultVarGuest = StringVar()
ResultVarGuest.set("")
ResultTextGuest = Message(root,textvariable = ResultVarGuest, width= rootWidth, relief = "flat", bg = "white")

ResultVarDraw = StringVar()
ResultVarDraw.set("")
ResultTextDraw = Message(root,textvariable = ResultVarDraw, width= rootWidth, relief = "flat", bg = "white")



#NextGameDays -------------
Box = Frame(root, bg= "grey95", height = rootHeight - buttonHeight-35, width = buttonWidth)

NextGameDayHeadVar = StringVar()
NextGameDayHead = Message(Box ,textvariable=NextGameDayHeadVar, bg = "grey95",width= int(buttonWidth), relief = FLAT)
NextGameDayHeadVar.set("Kommender Spieltag")


NextGameDayVar = StringVar()
NextGameDayText = Message(Box ,textvariable=NextGameDayVar, bg = "grey95",width= int(buttonWidth), relief = FLAT, font = ('TkDefaultFont', 10))
NextGameDaySetUp()


#Pack Widgets---------------------

#Buttons
buttonCrawler.pack()
buttonAlgorithm.pack()
buttonCalculate.pack()

#DropDownMenu
dropdownHome.pack()
dropdownGuest.pack()


#Text
InfoText.pack()
ResultTextHome.pack()
ResultTextGuest.pack()
ResultTextDraw.pack()
NextGameDayText.pack()
NextGameDayHead.pack()
Box.pack()


#Place Widgets---------------------

#Buttons
buttonCrawler.place(height = buttonHeight, width = buttonWidth, x = 0, y = 0)
buttonAlgorithm.place(height = buttonHeight, width = buttonWidth, x = buttonWidth, y = 0)
buttonCalculate.place(height = buttonHeight, width = buttonWidth, x = 2*buttonWidth, y = 0)



#DropDownMenu
dropdownHome.place(height= dropdownHeight, width = dropdownWidth, x = 0, y = buttonHeight)
dropdownGuest.place(height= dropdownHeight, width = dropdownWidth, x = dropdownWidth, y = buttonHeight)


#Text 
InfoText.place(x = 0, y = rootHeight-30)
ResultTextHome.place(x = 50, y = rootHeight/3+50)
ResultTextGuest.place(x = buttonWidth+50, y = rootHeight/3+50)
ResultTextDraw.place(x = rootWidth/4, y = rootHeight/2+50)
Box.place(x = 2*buttonWidth, y= buttonHeight)
NextGameDayHead.place(x = 60, y = 0)
NextGameDayText.place(x = 0, y = 35)
#Start Mainloop of the Root---------------------
root.mainloop()
