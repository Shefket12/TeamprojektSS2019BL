#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from Crawlerpy import *
from ProbabilityAlgorithm import *


#Methods for Buttons---------------------
def Crawler():
    
    DCrawler.clear_Matchdays()
    global crawlerConfigPopUp
    crawlerConfigPopUp = Toplevel()
    crawlerConfigPopUp.wm_title("Crawler Settings")
    crawlerConfigPopUp.geometry(str(popUpWidth)+"x"+str(popUpHeight))
    
    l = Label(crawlerConfigPopUp, text="Select Seasons")
    l.grid(row=1, column=0)
    
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    
    Saison18 = Checkbutton(crawlerConfigPopUp, text="Saison 18/19", variable=var1,onvalue = 1, offvalue = 0)
    Saison18.grid(row=1, sticky=W)
    
    Saison17 = Checkbutton(crawlerConfigPopUp, text="Saison 17/18", variable=var2, onvalue = 1, offvalue = 0)
    Saison17.grid(row=2, sticky=W)
    
    Saison16 = Checkbutton(crawlerConfigPopUp, text="Saison 16/17", variable=var3, onvalue = 1, offvalue = 0)
    Saison16.grid(row=3, sticky=W)
    
    Saison15 = Checkbutton(crawlerConfigPopUp, text="Saison 15/16", variable=var4, onvalue = 1, offvalue = 0)
    Saison15.grid(row=4, sticky=W)
    
    b = Button(crawlerConfigPopUp, text= "Okay", command =lambda: RunCrawler(var1, var2, var3, var4))
    b.grid(row=5, column=0)
    
    def RunCrawler(var1, var2, var3, var4):
        
        if(var1.get() == 1):
            DCrawler.add_Season(2018,1,35) 
            
        if(var2.get() == 1):
            DCrawler.add_Season(2017,1,35)  
            
        if(var3.get() == 1):
            DCrawler.add_Season(2016,1,35) 
            
        if(var4.get() == 1):
            DCrawler.add_Season(2015,1,35) 
            
        DCrawler.write_CSVFile()
        
        InfoText.configure(state = "normal")
        InfoText.delete("1.0",END)
        InfoText.insert("end", "Start Algortihm-Training for the Calculation")
        InfoText.configure(state = "disabled")
    

    
def AlgorithmTraining():
    CalcAlgo.processData("BundesligaData.csv")
    CalcAlgo.printData()
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Choose Algorithm and Teams for the Calculation")
    InfoText.configure(state = "disabled")
    

def Calculate():
    
    if (str(variableHome.get()) != "Home") and (str(variableGuest.get()) != "Guest") and(str(variableHome.get())!= str(variableGuest.get())) and (str(variableAlgorithm.get()) != "Algorithm Selection"):
        
        result = CalcAlgo.getBaseAlgorithm(str(variableHome.get()), str(variableGuest.get()))
        print(result[0])
        print(result[1])
        
        #Delete InfoText
        InfoText.configure(state = "normal")
        InfoText.delete("1.0",END)
        InfoText.insert("end", "")
        InfoText.configure(state = "disabled")
        
        #Calculate
        
        
        #Insert ResultText
        ResultText.configure(state = "normal")
        ResultText.delete("1.0",END)
        ResultText.insert("end", "Home: "+ str(result[0])+"\n"+"Guest: "+str(result[1]))
        ResultText.configure(state = "disabled")
    else: return

#Initialize variables for calculation
CalcAlgo = Algorithm()
DCrawler = DataCrawler("BundesligaData.csv")

#Initialize Root-Window---------------------     
root = Tk()
root.title("Softwareprojekt Bundesliga SS19 GUI")

#Numbers for Root and Widgets---------------------
rootWidth = 800
rootHeight = 450
rootResulution = str(rootWidth)+"x"+str(rootHeight)
root.geometry(rootResulution)
root.resizable(width = False, height = False)

popUpHeight = 150
popUpWidth = 200

buttonHeight = 30
buttonWidth = rootWidth/2

dropdownHeight = buttonHeight
dropdownWidth = rootWidth/2


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


# In[ ]:





# In[ ]:




