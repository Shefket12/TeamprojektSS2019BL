#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
from Crawler.Crawlerpy import *
from Data.TeamIdentification import *
from tkinter import *
from Algorithm.ProbabilityAlgorithm import *


#Methods for Buttons---------------------
def Crawler():
    DCrawler.clear_Matchdays()
    global crawlerConfigPopUp
    crawlerConfigPopUp = Toplevel()
    crawlerConfigPopUp.wm_title("Crawler Einstellungen")
    crawlerConfigPopUp.geometry(str(popUpWidth)+"x"+str(popUpHeight))
    
    Saison18value = IntVar()
    Saison18start = StringVar()
    Saison18end = StringVar()
    Saison17value  = IntVar()
    Saison17start = StringVar()
    Saison17end = StringVar()
    Saison16value  = IntVar()
    Saison16start = StringVar()
    Saison16end = StringVar()
    Saison15value  = IntVar()
    Saison15start = StringVar()
    Saison15end = StringVar()
    
    #Saison 18
    CheckSaison18 = Checkbutton(crawlerConfigPopUp, text="Saison 18/19", variable=Saison18value,onvalue = 1, offvalue = 0)
    CheckSaison18.grid(row=1, sticky=W)
    
    Label(crawlerConfigPopUp, text="Spieltag").grid(row=1, column = 3, sticky=W)
    
    entryFirstDaySaison18 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison18start)
    entryFirstDaySaison18.grid(row=1, column = 4, sticky=W)
    entryFirstDaySaison18.insert(0, "1")
    
    Label(crawlerConfigPopUp, text="bis").grid(row=1, column = 5, sticky=W)
    
    entryLastDaySaison18 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison18end)
    entryLastDaySaison18.grid(row=1, column = 6, sticky=W)
    entryLastDaySaison18.insert(0, "34")
   
    #Saison 17
    
    CheckSaison17 = Checkbutton(crawlerConfigPopUp, text="Saison 17/18", variable=Saison17value, onvalue = 1, offvalue = 0)
    CheckSaison17.grid(row=2, sticky=W)
    
    Label(crawlerConfigPopUp, text="Spieltag").grid(row=2, column = 3, sticky=W)
    
    entryFirstDaySaison17 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison17start)
    entryFirstDaySaison17.grid(row=2, column = 4, sticky=W)
    entryFirstDaySaison17.insert(0, "1")
    
    Label(crawlerConfigPopUp, text="bis").grid(row=2, column = 5, sticky=W)
    
    entryLastDaySaison17 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison17end)
    entryLastDaySaison17.grid(row=2, column = 6, sticky=W)
    entryLastDaySaison17.insert(0, "34")
    
    #Saison 16
    CheckSaison16 = Checkbutton(crawlerConfigPopUp, text="Saison 16/17", variable=Saison16value , onvalue = 1, offvalue = 0)
    CheckSaison16.grid(row=3, sticky=W)
    
    Label(crawlerConfigPopUp, text="Spieltag").grid(row=3, column = 3, sticky=W)
    
    entryFirstDaySaison16 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison16start)
    entryFirstDaySaison16.grid(row=3, column = 4, sticky=W)
    entryFirstDaySaison16.insert(0, "1")
    
    Label(crawlerConfigPopUp, text="bis").grid(row=3, column = 5, sticky=W)
    
    entryLastDaySaison16 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison16end)
    entryLastDaySaison16.grid(row=3, column = 6, sticky=W)
    entryLastDaySaison16.insert(0, "34")
    
    #Saison 15
    CheckSaison15 = Checkbutton(crawlerConfigPopUp, text="Saison 15/16", variable=Saison15value , onvalue = 1, offvalue = 0)
    CheckSaison15.grid(row=4, sticky=W)
    
    Label(crawlerConfigPopUp, text="Spieltag").grid(row=4, column = 3, sticky=W)
    
    entryFirstDaySaison15 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison15start)
    entryFirstDaySaison15.grid(row=4, column = 4, sticky=W)
    entryFirstDaySaison15.insert(0, "1")
    
    Label(crawlerConfigPopUp, text="bis").grid(row=4, column = 5, sticky=W)
    
    entryLastDaySaison15 = Entry(crawlerConfigPopUp, width = 2, textvariable=Saison15end)
    entryLastDaySaison15.grid(row=4, column = 6, sticky=W)
    entryLastDaySaison15.insert(0, "34")
    
    #Button
    buttonRunCrawler = Button(crawlerConfigPopUp,
                              text= "Crawler starten",
                              command = combine_funcs(lambda: RunCrawler(Saison18value,
                                                                        Saison18start,
                                                                         Saison18end,
                                                                         Saison17value,
                                                                         Saison17start,
                                                                         Saison17end,
                                                                         Saison16value, 
                                                                         Saison16start,
                                                                         Saison16end,
                                                                         Saison15value,
                                                                         Saison15start,
                                                                         Saison15end),
                                                      crawlerConfigPopUp.destroy))
    buttonRunCrawler.grid(row=5)
  
    def RunCrawler(Saison18value,
                   Saison18start,
                   Saison18end,
                   Saison17value,
                   Saison17start,
                   Saison17end,
                   Saison16value,
                   Saison16start,
                   Saison16end,
                   Saison15value,
                   Saison15start,
                   Saison15end):
        
        if(Saison15value.get() == 1):
            DCrawler.add_Season(2015,int(Saison15start.get()),int(Saison15end.get())) 
            
        if(Saison16value.get() == 1):
            DCrawler.add_Season(2016,int(Saison16start.get()),int(Saison16end.get()))  
            
        if(Saison17value.get() == 1):
            DCrawler.add_Season(2017,int(Saison17start.get()),int(Saison17end.get())) 
            
        if(Saison18value.get() == 1):
            DCrawler.add_Season(2018,int(Saison18start.get()),int(Saison18end.get())) 
            
        DCrawler.write_CSVFile()
        InfoText.configure(state = "normal")
        InfoText.delete("1.0",END)
        InfoText.insert("end", "Start Algortihm-Training for the Calculation")
        InfoText.configure(state = "disabled")
        
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
    
def AlgorithmTraining():
    CalcAlgo.processData(CVS_Path)
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Choose Algorithm and Teams for the Calculation")
    InfoText.configure(state = "disabled")
    

def Calculate():
    
    if (str(variableHome.get()) != "Home") and (str(variableGuest.get()) != "Guest") and(str(variableHome.get())!= str(variableGuest.get())) and (str(variableAlgorithm.get()) != "Algorithm Selection"):
        
        print(get_TeamID(str(variableHome.get())))
        print(get_TeamID(str(variableGuest.get())))
        result = CalcAlgo.getBaseAlgorithm(get_TeamID(str(variableHome.get())), get_TeamID(str(variableGuest.get())))
        
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
root.title("Softwareprojekt Bundesliga SS19 GUI")

#Numbers for Root and Widgets---------------------
rootWidth = 800
rootHeight = 450
rootResulution = str(rootWidth)+"x"+str(rootHeight)
root.geometry(rootResulution)
root.resizable(width = False, height = False)

popUpHeight = 140
popUpWidth = 280

buttonHeight = 30
buttonWidth = rootWidth/2

dropdownHeight = buttonHeight
dropdownWidth = rootWidth/2

#Initialize variables for calculation

CVS_Path = "Data/BundesligaData.csv" 

CalcAlgo = Algorithm()
DCrawler = DataCrawler(CVS_Path)


# Initialize Widgets---------------------

#Buttons
buttonCrawler = Button(root, text = "Crawler", command = Crawler)
buttonAlgorithm = Button(root, text = "Run Algorithm-Training", command = AlgorithmTraining)
buttonCalculate = Button(root, text = "Calculation", command = Calculate)

#DropDownMenu
variableHome = StringVar(root)
variableGuest = StringVar(root)
variableAlgorithm = StringVar(root)
variableHome.set("Home") 
variableGuest.set("Guest") 
variableAlgorithm.set("Algorithm Selection")

dropdownAlgorithm = OptionMenu(root, variableAlgorithm, "Minimaler Vorhersage-Algorithmus")
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
dropdownAlgorithm.pack()

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
dropdownAlgorithm.place(height= dropdownHeight, width = dropdownWidth, x = 0, y = buttonHeight)

#Text
ResultText.place(x = 250, y = rootHeight/2)

#Start Mainloop of the Root---------------------
root.mainloop()
