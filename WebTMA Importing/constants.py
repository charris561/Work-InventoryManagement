#This file contants constants to be used in the WebTMA_Import_Script
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/7/2022

#file names (Inventory spreadsheet name and data sheet name defined in WebTMA_Import_Script.py)
LOGFILE_PATH = "Log Files\ImportedAssets.csv"
LOGFILE_HEADERS = ['Tag Number', 'Description', 'Building Name', 'Area #', 'Serial #']

#pyautogui needed data ("If using on another system, change these values!")
#Use pyautogui.displayMousePosition() to display mouse position and $py -m pip install pillow to get the required dependency if needed
WEBTMA_WHITESPACE_COORDS_x = 1600
WEBTMA_WHITESPACE_COORDS_y = 710
ORGANIZATION_BUTTON_COORDS_x = 50
ORGANIZATION_BUTTON_COORDS_y = 969
ASSET_BUTTON_COORDS_x = 50
ASSET_BUTTON_COORDS_y = 475
ADD_BUTTON_COORDS_x = 187
ADD_BUTTON_COORDS_y = 140
TAG_NUMBER_FIELD_COORDS_x = 810
TAG_NUMBER_FIELD_COORDS_y = 196
LOCATION_ID_FIELD_COORDS_x = 813
LOCATION_ID_FIELD_COORDS_y = 220
DESCRIPTION_FIELD_COORDS_x = 1185
DESCRIPTION_FIELD_COORDS_y = 192
LOCATION_ID_FIRST_RESULT_x = 827
LOCATION_ID_FIRST_RESULT_y = 239
MANUFACTURER_FIELD_COORDS_x = 1182
MANUFACTURER_FIELD_COORDS_y = 292
MANUFACTURER_FIRST_RESULT_x = 1182
MANUFACTURER_FIRST_RESULT_y = 313
MODEL_NUM_FIELD_COORDS_x = 1175
MODEL_NUM_FIELD_COORDS_y = 317
SERIAL_NUM_FIELD_COORDS_x = 1176
SERIAL_NUM_FIELD_COORDS_y = 342
WARRANTY_EXPIRES_FIELD_COORDS_x = 1178
WARRANTY_EXPIRES_FIELD_COORDS_y = 399
INVENTORY_DATE_FIELD_COORDS_x = 1179
INVENTORY_DATE_FIELD_COORDS_y = 450
ASSIGNED_TO_FIELD_COORDS_x = 1172
ASSIGNED_TO_FIELD_COORDS_y = 478
QUANTITY_FIELD_COORDS_x = 1173
QUANTITY_FIELD_COORDS_y = 548
COMMENT_FIELD_COORDS_x = 827
COMMENT_FIELD_COORDS_y = 626
REPAIR_CENTER_TAB_COORDS_x = 530
REPAIR_CENTER_TAB_COORDS_y = 167
ADD_REPAIR_CENTER_BUTTON_COORDS_x = 218
ADD_REPAIR_CENTER_BUTTON_COORDS_y = 261
REPAIR_CENTER_IT_CHECKBOX_COORDS_x = 752
REPAIR_CENTER_IT_CHECKBOX_COORDS_y = 538
REPAIR_CENTER_SAVE_BUTTON_COORDS_x = 1000
REPAIR_CENTER_SAVE_BUTTON_COORDS_y = 800
WEBTMA_SAVE_ASSET_BUTTON_COORDS_x = 907
WEBTMA_SAVE_ASSET_BUTTON_COORDS_y = 140
DEPARTMENT_CODE = "IT-ADMINISTRATIVE OPERATIONS"
DEPARTMENT_FIELD_COORDS_x = 808
DEPARTMENT_FIELD_COORDS_y = 346
