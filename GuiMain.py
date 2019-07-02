#!/usr/bin/env python
# coding: utf-8

from Crawler.Crawlerpy import *
from Data.TeamIdentification import *
from tkinter import *
from Algorithm.ProbabilityAlgorithm import *


#Methods for Buttons---------------------

def Crawler():
    BLCrawler.get(2012,2018)
    InfoVar.set("Konfigurieren Sie ihre Berechnung in den Einstellungen")
    
       
def AlgorithmConfiguration():
    
    InfoVar.set("Wählen Sie einen Algorithmus und den gewünschten Datensatz. Drücken Sie anschließend aus 'Bestätigen'")
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
    entryFirstSeason.insert(0, "2012")
    
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
        
    CalcAlgo.processData(CVS_Path, FirstSeason, LastSeason, FirstGameDay, LastGameDay)
    
def Calculate():
    
    if (CalcAlgo.hasMatches()):
        if(CalcAlgo.algorithmIndex != -1):
            if (str(variableHome.get()) != "Heim") and (str(variableGuest.get()) != "Gast"):
                if(str(variableHome.get())!= str(variableGuest.get())):
                
                    result = CalcAlgo.getResult(get_TeamID(str(variableHome.get())), get_TeamID(str(variableGuest.get())), CVS_Path)
        
                    print(result[0])
                    print(result[1])
                    print(result[2])
                    print("Test: "+str(result[0]+result[1]+result[2]))
        
                    #Delete InfoText
                    InfoVar.set("")
        
                    #Calculate
        
                    #Insert ResultText
                    ResultText.configure(state = "normal")
                    ResultText.delete("1.0",END)
                    ResultText.insert("end", str(variableHome.get())+": \t"+ str(result[0]*100)+" %\n"+str(variableGuest.get())+": \t"+str(result[1]*100)+" %\n"+"Unentschieden: \t"+str(result[2]*100)+" %")
                    ResultText.configure(state = "disabled")
                else:
                    InfoVar.set("Wählen Sie zwei unterschiedliche Mannschaften aus!")
            else:
                InfoVar.set("Wählen Sie zwei Mannschaften aus!")
        else:
            InfoVar.set("Sie haben keinen Algorithmus ausgewählt. Gehen Sie auf 'Einstellungen' und treffen Sie ein Auswahl")
    else:
        InfoVar.set("Es gibt keine Daten für die Berechnung! Starten Sie den Crawler und konfigurieren Sie die Daten in den Einstellungen.")

def NextGameDaySetUp(var):
    overall = "Kommender Spieltag:\n"
    
    for i in range(1,10):
        overall = overall +"Spiel "+str(i)+": \n"
    
    var.set(overall)
    
    return
    
    
#Initialize Root-Window---------------------     
root = Tk()
root.title("Softwareprojekt Bundesliga")

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

CalcAlgo = ProbabilityAlgorithm()
BLCrawler = DataCrawler(CVS_Path)


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

dropdownHome = OptionMenu(root, variableHome, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "1. FC Nürnberg", "FC Schalke 04", "VfB Stuttgart", "VfL Wolfsburg")
dropdownGuest = OptionMenu(root, variableGuest, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "1. FC Nürnberg", "FC Schalke 04", "VfB Stuttgart", "VfL Wolfsburg")

#Text
InfoVar = StringVar()
InfoVar.set("Starten Sie den Crawler")
InfoText = Message(root,textvariable = InfoVar, width= rootWidth, relief = "flat", fg = "red")



ResultText = Text(root, height=3, width= rootWidth, relief= "flat")
ResultText.insert("end", "")
ResultText.configure(state="disabled")

NextGameDayVar = StringVar()
NextGameDayText = Message(root,textvariable=NextGameDayVar, width= int(buttonWidth), relief = FLAT)
NextGameDaySetUp(NextGameDayVar)


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
ResultText.pack()
NextGameDayText.pack()

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
ResultText.place(x = rootWidth/6, y = rootHeight/2)
NextGameDayText.place(x = 2*buttonWidth, y = buttonHeight)

#Start Mainloop of the Root---------------------
root.mainloop()
