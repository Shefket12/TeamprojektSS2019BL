# Teamprojekt

In General:
This Project uses online Data to project probabilities for the different outcomes of a football(soccer) match between two teams. Our project is applied for the '1.Bundesliga' in germany.

Summary:
1. Crawler
2. Graphical User Interface(GUI)
3. Algortihm\\

1. CRAWLER
The crawler has two main functions: 
  1. To crawl the wanted data from past games and write it into a csv-file
  2. To crawl the upcoming fixtures of the Bundesliga.

The method 'getSeasons' uses the parameters 'FirstSeason' and 'LastSeason' as a range, for the seasons which should be fetched. The method turns to the page 'openligadb.de' with the given parameters and selects the following data from the games within the range between 'FirstSeason' and 'LastSeason': Date, Season, Matchday, HometeamID, AwayteamID, Hometeamscore and Awayteamscore.
All these informations will then be written in to a csv-file line by line, called 'BundesligaData'. This file can be found in the folder 'Data'

'getNextSeason' has the same modularity as 'getSeasons' but with two differences: 1. If only crawls games for one season. 2. It doesn't fetch any scores. This method has these two important differences, because it is used to crawl games, which haven't been played yet. The games which will be crawled in this method will be written into an extra csv-file in the folder 'Data', called 'nextSeason'. 

The Crawler-class has another two methods, which are shortly explained: 
'clear' is just a method to delet all the data in the csv-file 'BundesligaData'.
'internet_on' is a boolean methods, which checks, if there is a working internet connection. Because of this, the methods 'getSeasons' and 'getNextSeason' throw an exception, if 'internet_on' returns the value false, which states: 'You should check your internet connection, before you proceed'.

2. GUI
The Graphical User Interface combines all classes and data and handles all inputs. The GUI has five buttons(these are mostly stated in german, because it was a german group tp the develop the program and it is applied for the german Bundesliga): 'Crawler', 'Einstellungen', 'Berechnung', 'Heim' and 'Gast'.
Here a closer definition of what those buttons do:
1.Crawler:
  The Crawler starts the method 'getSeasons' in the class Crawler. This means, this button will trigger the method, which will 'crawl     all the data of the previous Bundesliga seasons and write it into the csv-file 'BundesligaData'.
2.Einstellungen:
  In 'Einstellungen' you can choose the data from which the probabilities will be calculated and also which algorithm will be used. In     particular this means, that you set four parameters(Firstseason, Lastseason, Firstmatchday, Lastmatchday) to a certain range. This       range will then be used in the calculations(Note, that the csv-file will not be changed! The code uses an Array with the selected       data). Also keep in mind to use valid input. The code won't work with chars or strings as input, but will with invalid integers as       input.
  Furthermore in 'Einstellungen' you can choose between the 'Basis Algorithmus' and the 'Poisson Regression'. The 'Basis                   Alogrithmus' just cumulates all results between two given teams and calculates, which team has won how many times, in relation to the   number of games played between these teams. This equals the probabilities the algorithm will give you.
  The 'Poisson Regression' uses, as it states in the name, the poisson regression to calculate the probabilites for either one team to     win or both teams to draw. It uses a pandas-dataframe, for the calculation. To sort out the trouble, that the TeamIDs are taken into     the calculations, the method 'replaceIDs' changes the IDs in the dataframe to the corresponding teamname, using the csv-file             'TeamIDs', which can be found in the folder 'Data'.
  FIY: You have two choose between one of the algorithms, because there is none set to default.
3.Berechnung
  Pretty simple: Calculates the probabilities with the given parameters, set in 'Einstellungen'
4.Heim and Gast
  With these buttons you choose between the current 18 Bundesligateams and determine, which will be home and which will be away, since     this plays a big part in football. Beware that you can not choose the same team as home and away at the same time! The GUI will tell     you to choose different teams. If you do choose the same teams nothing happens.
On the right hand side of the GUI you can see the upcoming matchday and the probabilities, based on the chosen data and algorithm. 

3. ALGORTIHM
The folder 'Algorithm' has five classes. One for each algorithm, two to parse the csv-file and one for the GUI to process the data.
The classes 'match' and 'parse_csv_data' are used to parse the data from the csv-file to a useable array in the program.
In '2.Gui/2.Einstellungen' the procedure of both algorithm was already explained, no need to do this here again.
With the class 'ProbabilityAlgorithm' the GUI has different tools to work with the data and handle the input. With 'setAlgorithm' it can differenciate between the two algorithms. 'setSeasons' uses the four parameters from 'Einstellungen' to set the range of selected data. 'processData' parses the csv-file into an array, using the 'parse_csv_data' and 'match' class. The methods 'printData', 'deleteData' and 'hasMatches' are self explanatory.
The main method of this class is the 'getResult'-method. It checks, which algorithm should be used for the calculation and then gives the data to the corresponding algorithm.



















Footnote: For the sophisticated people who are using Apple, there is an extra GUIMacOS version
