from tkinter import *

#Methods for Buttons---------------------
def Crawler():
    print("toDo: Crawler")
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Start Algortihm-Training for the Calculation")
    InfoText.configure(state = "disabled")
    
    
def AlgorithmTraining():
    print("toDo: AlgorithmTraining")
    InfoText.configure(state = "normal")
    InfoText.delete("1.0",END)
    InfoText.insert("end", "Choose Teams for the Calculation")
    InfoText.configure(state = "disabled")
    

def Calculate():
    if (str(variableHome.get()) != "Home") and (str(variableGuest.get()) != "Guest") and (str(variableHome.get())!= str(variableGuest.get())):
        print("toDo: Calculation")
        
        #Delete InfoText
        InfoText.configure(state = "normal")
        InfoText.delete("1.0",END)
        InfoText.insert("end", "")
        InfoText.configure(state = "disabled")
        
        #Insert ResultText
        ResultText.configure(state = "normal")
        ResultText.delete("1.0",END)
        ResultText.insert("end", "Home: "+"\n"+"Guest: ")
        ResultText.configure(state = "disabled")
    else: return


        
#Initialize Root-Window---------------------     
root = Tk()
root.title("Softwareprojekt Bundesliga SS19 GUI v1.1")

#Numbers for Root and Widgets---------------------
rootWidth = 800
rootHeight = 450
rootResulution = str(rootWidth)+"x"+str(rootHeight)
root.geometry(rootResulution)
root.resizable(width = False, height = False)

buttonHeight = 30
buttonWidth = rootWidth/3

dropdownHeight = buttonHeight
dropdownWidth = rootWidth/2


# Initialize Widgets---------------------

#Buttons
buttonCrawler = Button(root, text = "Run Crawler", command = Crawler)
buttonAlgorithm = Button(root, text = "Run Algorithm-Training", command = AlgorithmTraining)
buttonCalculate = Button(root, text = "Calculation", command = Calculate)

#DropDownMenu
variableHome = StringVar(root)
variableGuest = StringVar(root)
variableHome.set("Home") 
variableGuest.set("Guest") 

dropdownHome = OptionMenu(root, variableHome, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer 04 Leverkusen", "1. FC Mainz 05", "Borussia Mönchengladbach", "FC Bayern München", "1. FC Nürnberg", "FC Schalke 04", "VFB Stuttgart", "VFL Wolfsburg")
dropdownGuest = OptionMenu(root, variableGuest, "FC Augsburg", "Hertha BSC", "Werder Bremen", "Borussia Dortmund", "Fortuna Düsseldorf", "Eintracht Frankfurt", "SC Freiburg", "Hannover 96", "TSG 1899 Hoffenheim", "RB Leipzig", "Bayer 04 Leverkusen", "1. FC Mainz 05", "Borussia Mönchengladbach", "FC Bayern München", "1. FC Nürnberg", "FC Schalke 04", "VFB Stuttgart", "VFL Wolfsburg")

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
buttonCalculate.place(height = buttonHeight, width = buttonWidth, x = 2* buttonWidth, y = 0)

#DropDownMenu
dropdownHome.place(height= dropdownHeight, width = dropdownWidth, x = 0, y = buttonHeight)
dropdownGuest.place(height= dropdownHeight, width = dropdownWidth, x = dropdownWidth, y = buttonHeight)

#Text
ResultText.place(x = 250, y = rootHeight/2)

#Start Mainloop of the Root---------------------
root.mainloop()

