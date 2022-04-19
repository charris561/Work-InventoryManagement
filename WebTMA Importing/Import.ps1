#This script will use a python script to programatically import data from the specified spreadsheet to WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/11/2022

echo "This script will import data from the specified spreadsheet to the WebTMA web app

Note: The excel document will need the columns specified in the python script although
the cells may be empty.
-----------------------------------------------------------------------------------------------
"

do {
    
    $sourceFile = Read-Host -Prompt 'Please enter the source spreadsheet name (example.xlsx)'
    $sourceSheet = Read-Host -Prompt 'Please enter the sheet name of the incoming data as it appears in excel'
    $userAnswer = Read-Host -Prompt "You entered $sourceFile and $sourceSheet, is this correct (y/n)?"

} while( $userAnswer -ne 'y')

python WebTMA_Import_Script.py $sourceFile $sourceSheet

Read-Host -Prompt "Press enter to exit"
