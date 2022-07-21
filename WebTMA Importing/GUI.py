#This class provides the methods for graphical elements
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 7/20/2022

import os
import GUI_Automation
import tkinter as tk
from tkinter import filedialog
import constants
from ExcelFunctions import getSheetNames

def getFilePath():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def getSheetName():
    return input("Please enter the name of the sheet in excel: ")

def cmdProgressBar(progress, total):

    '''
    This function displays a progress bar for the current operation in the command prompt
    Function written by NeuralNine on Youtube: https://www.youtube.com/watch?v=x1eaT88vJUA
    '''

    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}", end="\r")

def getUserConfirm(selectedOption):
    '''
    Function get user confirmation for their selected option
    '''
    userVerfied = None
    while (userVerfied != True and userVerfied != False):
        
        confirmation = input(f"You selected {selectedOption}; is this correct? (y/n): ")
        
        if (confirmation == 'y' or confirmation == 'Y'):
            userVerfied = True
        elif (confirmation == 'n' or confirmation == 'N'):
            userVerfied = False
        else:
            print("Invalid selection.")

    return userVerfied

def cmdMenu(incomingAsset_List):

    '''
    This function displays a menu in the command prompt
    '''

    userChoice = None

    while(userChoice != '6'):
        #clears the screen
        os.system('cls')

        searchParam = None
        searchParamChoice = None
        userConfirm = None

        title = """Welcome to the UCCS OIT Inventory Importing Application
------------------------------
Author: Caleb Harris
Position: OIT Services Professional
Date Created: 7/20/2022
------------------------------"""
        mainMenu = """------------------------------
1. Get Mouse Coordinates
2. Start Navigation to Asset Window
3. Add new inventory
4. Update existing inventory
5. Help
6. Exit
------------------------------
""" 
        searchParamOptions = """------------------------------
1. Serial Number
2. Tag Number
------------------------------"""

        print(f"{title}\n{mainMenu}")

        userChoice = input("Please enter menu option number: ")

        if (userChoice == '1'):
            print("Getting mouse position...\n")
            GUI_Automation.getMouseCoords()
        
        elif (userChoice == '2'):
            userConfirm = getUserConfirm("\"Navigation to Asset\"")
            if (userConfirm == True):
                GUI_Automation.startNavToAsset()
        
        elif (userChoice == '3'):
            userConfirm = getUserConfirm("\"Add New Inventory\"")
            if (userConfirm == True):
                GUI_Automation.inventoryAsset(incomingAsset_List)
        
        elif (userChoice == '4'):
            while (searchParamChoice != '1' and searchParamChoice != '2'):
                print(searchParamOptions)
                searchParamChoice = input("What search parameter would you like to use? ")

                if (searchParamChoice == '1'):
                    searchParam = "Serial #"
                elif (searchParamChoice == '2'):
                    searchParam = "Tag Number"
                else:
                    print ("Invalid Option.")

            userConfirm = getUserConfirm(f"\"Upate Assets (Search Parameter = {searchParam})\"")
            if (userConfirm == True):
                GUI_Automation.updateAsset(incomingAsset_List, searchParam)
            
        elif (userChoice == '5'):
            print ("Displaying help window...'n")
        
        elif (userChoice == '6'):
            print ("Exiting...\n")
        
        else:
            print("Unkown menu choice. Please select another option.")

        input("Press any key to continue.")

def displayExcelSheetNames():
    print(f"------------------------------\nAvailable Sheets for file: {constants.INVENTORY_SPREADSHEET_FILENAME}")
    print(f"{getSheetNames()}\n------------------------------\n")

