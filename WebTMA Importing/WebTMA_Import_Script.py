#This script will use the pyautogui library to programatically import data from the specified spreadsheet to WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/7/2022

#WebTMA URL: https://facserv.uccs.edu/TMALogin/login.aspx
#pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/
#openpyxl documentation: https://openpyxl.readthedocs.io/en/stable/
#How to install pyautogui in powershell: py -m pip install pyautogui

#Imports
from time import sleep
import ExcelFunctions
import constants
import GUI

#Main Script
incomingAsset_List = []
ExcelFunctions.getDataFromExcel(incomingAsset_List)
GUI.cmdMenu(incomingAsset_List)
