#This class provides the methods to control WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/9/2022

from datetime import date
import constants
import pyautogui
from Asset import Asset
import ExcelFunctions
import LOG
import time

class GUI_Automation:

    #pyautogui configuration
    pyautogui.PAUSE = .5
    pyautogui.FAILSAFE = True

    def startNavToAsset():
        '''
        This function will navigate to the "new asset" page of web tma
        '''
        pyautogui.PAUSE = 1
        pyautogui.click(constants.WEBTMA_WHITESPACE_COORDS_x, constants.WEBTMA_WHITESPACE_COORDS_y) #clicks whitespace to bring WebTMA window in focus
        pyautogui.click(constants.ORGANIZATION_BUTTON_COORDS_x, constants.ORGANIZATION_BUTTON_COORDS_y)
        pyautogui.click(constants.ASSET_BUTTON_COORDS_x, constants.ASSET_BUTTON_COORDS_y)

    def inventoryAsset(incomingAsset_List):

        '''
        This function contains the main logic to fill fields and inventory devices
        '''
        LOG.defineHeaders()

        for currentAsset in incomingAsset_List:
            
            #data entry for mandatory fields
            pyautogui.PAUSE = 1
            pyautogui.click(constants.ADD_BUTTON_COORDS_x, constants.ADD_BUTTON_COORDS_y)
            time.sleep(2)
            pyautogui.PAUSE = .7
            pyautogui.click(constants.TAG_NUMBER_FIELD_COORDS_x, constants.TAG_NUMBER_FIELD_COORDS_y)
            pyautogui.write(currentAsset.getAssetTag())
            pyautogui.click(constants.LOCATION_ID_FIELD_COORDS_x, constants.LOCATION_ID_FIELD_COORDS_y)
            pyautogui.write(currentAsset.getLocationID())
            pyautogui.press('enter')
            pyautogui.press('tab', 2, .5)
            pyautogui.PAUSE = .5
            pyautogui.click(constants.DESCRIPTION_FIELD_COORDS_x, constants.DESCRIPTION_FIELD_COORDS_y)
            pyautogui.write(currentAsset.getDescription())
            pyautogui.press('tab')
            pyautogui.write(currentAsset.getType())
            time.sleep(.5)
            pyautogui.press('enter')
            pyautogui.click(constants.WEBTMA_WHITESPACE_COORDS_x, constants.WEBTMA_WHITESPACE_COORDS_y)

            #data entry for non-mandatory fields
            if (currentAsset.getManufacturer() != None):
                pyautogui.click(constants.MANUFACTURER_FIELD_COORDS_x, constants.MANUFACTURER_FIELD_COORDS_y)
                pyautogui.click(constants.MANUFACTURER_FIELD_COORDS_x, constants.MANUFACTURER_FIELD_COORDS_y)
                pyautogui.write(currentAsset.getManufacturer())
                pyautogui.press('tab')
                pyautogui.click(constants.WEBTMA_WHITESPACE_COORDS_x, constants.WEBTMA_WHITESPACE_COORDS_y)

            if (currentAsset.getModelNum() != None):
                pyautogui.click(constants.MODEL_NUM_FIELD_COORDS_x, constants.MODEL_NUM_FIELD_COORDS_y)
                pyautogui.write(f"{currentAsset.getModelNum()}")

            if (currentAsset.getSerialNum() != None):
                pyautogui.click(constants.SERIAL_NUM_FIELD_COORDS_x, constants.SERIAL_NUM_FIELD_COORDS_y)
                pyautogui.write(f"{currentAsset.getSerialNum()}")

            if (currentAsset.getWarrantyDate() != None):
                pyautogui.click(constants.WARRANTY_EXPIRES_FIELD_COORDS_x, constants.WARRANTY_EXPIRES_FIELD_COORDS_y)
                pyautogui.write(currentAsset.getWarrantyDate())
                
            pyautogui.click(constants.INVENTORY_DATE_FIELD_COORDS_x, constants.INVENTORY_DATE_FIELD_COORDS_y)
            pyautogui.write(f"{date.today()}")

            if (currentAsset.getUserAssignedTo() != None):
                pyautogui.click(constants.ASSIGNED_TO_FIELD_COORDS_x, constants.ASSIGNED_TO_FIELD_COORDS_y)
                pyautogui.write(currentAsset.getUserAssignedTo())

            if (currentAsset.hasQuantity()):
                if (currentAsset.getQuantity() != None):
                    pyautogui.click(constants.QUANTITY_FIELD_COORDS_x, constants.QUANTITY_FIELD_COORDS_y)
                    pyautogui.write(f"{currentAsset.getQuantity()}")

            if (currentAsset.getComment() != None):
                pyautogui.click(constants.COMMENT_FIELD_COORDS_x, constants.COMMENT_FIELD_COORDS_y)
                pyautogui.write(currentAsset.getComment())

            #set repair center
            pyautogui.PAUSE = 1.5
            pyautogui.click(constants.REPAIR_CENTER_TAB_COORDS_x, constants.REPAIR_CENTER_TAB_COORDS_y)
            pyautogui.click(constants.ADD_REPAIR_CENTER_BUTTON_COORDS_x, constants.ADD_REPAIR_CENTER_BUTTON_COORDS_y)
            pyautogui.click(constants.REPAIR_CENTER_IT_CHECKBOX_COORDS_x, constants.REPAIR_CENTER_IT_CHECKBOX_COORDS_y)
            pyautogui.click(constants.REPAIR_CENTER_SAVE_BUTTON_COORDS_x, constants.REPAIR_CENTER_SAVE_BUTTON_COORDS_y)

            #save the asset
            pyautogui.PAUSE = 1.5
            pyautogui.click(constants.WEBTMA_SAVE_ASSET_BUTTON_COORDS_x, constants.WEBTMA_SAVE_ASSET_BUTTON_COORDS_y)

            #pause before going to next asset
            time.sleep(2)

            #log that asset was imported successfully
            LOG.logImport(currentAsset)

    def updateAsset(incomingAsset_List, searchParam):
        '''
        This function will be used to update specific fields in WebTMA for existing data in WebTMA
        using a passed in search parameter.
        '''
        #pyautogui.displayMousePosition(); return
        for currentAsset in incomingAsset_List:
            
            #search for asset
            pyautogui.PAUSE = 1
            pyautogui.click(constants.SEARCH_BUTTON_COORDS_x, constants.SEARCH_BUTTON_COORDS_y)
            
            #set query in WebTMA to Tag Number > Contains > {searchParam} from list
            time.sleep(1)
            pyautogui.click(constants.SEARCH_SEARCHBY_FIELD_x, constants.SEARCH_SEARCHBY_FIELD_y, 2)
            
            #search by tag number
            if (searchParam == "Tag Number"):
                pyautogui.write("Tag Number")
                pyautogui.press('tab')
                pyautogui.write("contains")
                pyautogui.press('tab')
                pyautogui.write(currentAsset.getAssetTag())
            
            elif (searchParam == "Serial #"):
                pyautogui.write("Serial #")
                pyautogui.press('tab')
                pyautogui.write("contains")
                pyautogui.press('tab')
                pyautogui.write(currentAsset.getSerialNum())

            #Add additional search parameters here eventually
            else:
                exceptionText = f"\"{searchParam}\" invalid search parameter for object {currentAsset}\n"
                raise Exception(exceptionText)

            pyautogui.click(constants.SEARCH_FIND_BUTTON_COORDS_x, constants.SEARCH_FIND_BUTTON_COORDS_y)

            time.sleep(1)
            #click on the first result and start editing the asset
            pyautogui.click(constants.SEARCH_FIRST_RESULT_x, constants.SEARCH_FIRST_RESULT_y)
            time.sleep(1.5)
            pyautogui.click(constants.EDIT_BUTTON_COORDS_x, constants.EDIT_BUTTON_COORDS_y)

            #edit fields
            if (currentAsset.getAreaNum() != None):
                pyautogui.click(constants.LOCATION_ID_FIELD_COORDS_x, constants.LOCATION_ID_FIELD_COORDS_y)
                pyautogui.click(constants.LOCATION_ID_FIELD_COORDS_x, constants.LOCATION_ID_FIELD_COORDS_y, 3, .5)
                pyautogui.write(currentAsset.getLocationID())
                time.sleep(1)
                pyautogui.press('enter')
                pyautogui.press('tab', 2, .5)

            else:
                raise Exception(f"Could not find fields to update for {currentAsset}")

            #save the asset and go to the next
            pyautogui.click(constants.WEBTMA_SAVE_ASSET_BUTTON_COORDS_x, constants.WEBTMA_SAVE_ASSET_BUTTON_COORDS_y)

            #log the updated asset
            LOG.logImport(currentAsset)
