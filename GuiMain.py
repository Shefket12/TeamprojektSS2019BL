#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8
from Crawler.Crawlerpy import *
from Data.TeamIdentification import *
from tkinter import *
from Algorithm.ProbabilityAlgorithm import *


#Methods for Buttons---------------------

def Crawler():
    
    BLCrawler.get(2014,2018)
    
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Start Algortihm-Training for the Calculation")
    InfoText.configure(state = "disabled")
    
    
    
def AlgorithmConfiguration():
    
    
    global AlgorithmConfigPopUp
    AlgorithmConfigPopUp = Toplevel()
    AlgorithmConfigPopUp.wm_title("Algorithmus Einstellung")
    AlgorithmConfigPopUp.geometry(str(popUpWidth)+"x"+str(popUpHeight))
    AlgorithmConfigPopUp.grid_rowconfigure(10, minsize=100)
    
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
    entryFirstSeason.insert(0, "2014")
    
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
                               command = (lambda : RunAlgorithmTraining(
                                   int(firstSeason.get()),
                                   int(lastSeason.get()),
                                   int(firstGameDay.get()),
                                   int(lastGameDay.get()),
                                   str(variableAlgorithm.get()))))
    buttonRunTraining.grid(row=4 ,column= 1)
    
    
    #Button: Close Configuration----------------------------------------------------------
    buttonCloseConfiguration = Button(AlgorithmConfigPopUp, text= "Verlassen",command = AlgorithmConfigPopUp.destroy)
    buttonCloseConfiguration.grid(row=4 ,column= 0)
    
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Choose Algorithm and Teams for the Calculation")
    InfoText.configure(state = "disabled")
    
def RunAlgorithmTraining(FirstSeason, LastSeason, FirstGameDay, LastGameDay, AlgorithmChoice):
    CalcAlgo.deleteData()
    
    #Basis Algorithm:
    if(AlgorithmChoice == "Basis Algorithmus"):
        CalcAlgo.setAlgorithm(0)
        CalcAlgo.processData(CVS_Path, FirstSeason, LastSeason, FirstGameDay, LastGameDay)
    elif((AlgorithmChoice == "Poisson Regression")):
        CalcAlgo.setAlgorithm(1)
        CalcAlgo.processData(CVS_Path, FirstSeason, LastSeason, FirstGameDay, LastGameDay)
    
def Calculate():
    
    if (str(variableHome.get()) != "Home") and (str(variableGuest.get()) != "Guest") and(str(variableHome.get())!= str(variableGuest.get())):
        
        print(get_TeamID(str(variableHome.get())))
        print(get_TeamID(str(variableGuest.get())))
        result = CalcAlgo.getResult(get_TeamID(str(variableHome.get())), get_TeamID(str(variableGuest.get())))
        
        print(result[0])
        print(result[1])
        print(result[2])
        
        #Delete InfoText
        InfoText.configure(state = "normal")
        InfoText.delete("1.0",END)
        InfoText.insert("end", "")
        InfoText.configure(state = "disabled")
        
        #Calculate
        
        #Insert ResultText
        ResultText.configure(state = "normal")
        ResultText.delete("1.0",END)
        ResultText.insert("end", "Home: "+ str(result[0])+"\n"+"Guest: "+str(result[1])+"\n"+"Draw: "+str(result[2]))
        ResultText.configure(state = "disabled")
    else: return



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

buttonHeight = 30
buttonWidth = rootWidth/2

dropdownHeight = buttonHeight
dropdownWidth = rootWidth/2

#Initialize variables for calculation

CVS_Path = "Data/BundesligaData.csv" 

CalcAlgo = ProbabilityAlgorithm()
BLCrawler = DataCrawler(CVS_Path)


# Initialize Widgets---------------------

#Buttons
buttonCrawler = Button(root, text = "Crawler", command = Crawler)
buttonAlgorithm = Button(root, text = "Algorithmus Einstellung", command = AlgorithmConfiguration)
buttonCalculate = Button(root, text = "Calculation", command = Calculate)

#DropDownMenu
variableHome = StringVar(root)
variableGuest = StringVar(root)
variableAlgorithm = StringVar(root)
variableHome.set("Home") 
variableGuest.set("Guest") 

dropdownHome = OptionMenu(root, variableHome, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "1. FC Nürnberg", "FC Schalke 04", "VfB Stuttgart", "VfL Wolfsburg")
dropdownGuest = OptionMenu(root, variableGuest, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer Leverkusen", "1. FSV Mainz 05", "Borussia Mönchengladbach", "FC Bayern", "1. FC Nürnberg", "FC Schalke 04", "VfB Stuttgart", "VfL Wolfsburg")

#Text
InfoText = Text(root, height=1, width= rootWidth, fg ="red")
InfoText.insert("end", "Run the Crawler for the Calculation")
InfoText.configure(state="disabled")

ResultText = Text(root, height=3, width= rootWidth)
ResultText.insert("end", "")
ResultText.configure(state="disabled")


#Pack Widgets---------------------

#Buttons
buttonCrawler.pack()
buttonAlgorithm.pack()
buttonCalculate.pack()

#DropDownMenu
dropdownHome.pack()
dropdownGuest.pack()


#Text
InfoText.pack(side = BOTTOM)
ResultText.pack()

#Place Widgets---------------------

#Buttons
buttonCrawler.place(height = buttonHeight, width = buttonWidth, x = 0, y = 0)
buttonAlgorithm.place(height = buttonHeight, width = buttonWidth, x = buttonWidth, y = 0)
buttonCalculate.place(height = buttonHeight, width = buttonWidth, x = buttonWidth, y = buttonHeight)

#DropDownMenu
dropdownHome.place(height= dropdownHeight, width = dropdownWidth, x = 0, y = 2*buttonHeight)
dropdownGuest.place(height= dropdownHeight, width = dropdownWidth, x = dropdownWidth, y = 2*buttonHeight)


#Text
ResultText.place(x = 250, y = rootHeight/2)

#Start Mainloop of the Root---------------------
root.mainloop()
