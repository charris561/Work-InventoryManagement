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

    data = [asset.getAssetTag(), asset.getDescription(), asset.getBuilding(), asset.getAreaNum(), asset.getSerialNum()]

    writer.writerow(data)
    file.close
