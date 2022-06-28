# This script will contain the methods to log data for asset inventory
# Author: Caleb Harris - UCCS OIT Services Professional
# Date Created: 4/12/2022

from asyncore import write
import csv
import constants
from Asset import Asset

def defineHeaders():
    '''
    This function will define headers for log file and create it if it does not exist
    '''
    file = open(constants.LOGFILE_PATH, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(constants.LOGFILE_HEADERS)
    file.close()

def logImport(asset):
    '''
    This function will write successfully imported files to the log file
    '''
    file = open(constants.LOGFILE_PATH, 'a', newline='')
    writer = csv.writer(file)

    if (asset.hasAssetTag() and asset.hasDescription() and asset.hasBuilding() and asset.hasAreaNum() and asset.hasSerialNum()):
        data = [asset.getAssetTag(), asset.getDescription(), asset.getBuilding(), asset.getAreaNum(), asset.getSerialNum()]
    elif (asset.hasAssetTag()):
        data = [asset.getAssetTag()]
    elif (asset.hasSerialNum()):
        data = [asset.getSerialNum()]
    else:
        data = "No information on object"

    writer.writerow(data)
    file.close
