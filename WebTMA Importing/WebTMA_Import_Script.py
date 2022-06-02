#This script will use the pyautogui library to programatically import data from the specified spreadsheet to WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/7/2022

#WebTMA URL: https://facserv.uccs.edu/TMALogin/login.aspx
#pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/
#openpyxl documentation: https://openpyxl.readthedocs.io/en/stable/
#Note: The inventory spreadsheet will need to be located in the same directory as this script and must be named as the constant for the spreadsheet is (constants.py). 
#How to install pyautogui in powershell: py -m pip install pyautogui

#Imports
import sys
import ExcelFunctions
import constants
from Asset import Asset
from GUI_Automation import GUI_Automation
import LOG

#define workbook information
#constants.INVENTORY_SPREADSHEET_FILENAME = f"Excel Documents\{sys.argv[1]}"
#constants.INCOMING_DATA_SHEETNAME = sys.argv[2]
constants.INVENTORY_SPREADSHEET_FILENAME = "C:\\Users\\charris4\\OneDrive - University of Colorado Colorado Springs\\Work\\Inventory Management\\Data\\Excel Documents\\Moving Equipment Sheet.xlsx"
constants.INCOMING_DATA_SHEETNAME = "Search By Serials"

#Functions

def guiAutomation(incomingAsset_List):
    '''
    This function will house the gui automation occuring with pyautogui
    '''
    #GUI_Automation.startNavToAsset()
    #GUI_Automation.inventoryAsset(incomingAsset_List)
    searchParameter = "Serial #"
    GUI_Automation.updateAsset(incomingAsset_List, searchParameter)

#Main Script
incomingAsset_List = []
ExcelFunctions.getDataFromExcel(incomingAsset_List)
guiAutomation(incomingAsset_List)
