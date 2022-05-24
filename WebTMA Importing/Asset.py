#This class describes an asset object to be imported into WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/8/2022

from distutils.command.build import build
from pickle import TRUE


class Asset:
    '''
    This class will define an Asset object
    '''
    #constructor fields from WebTMA fields
    def __init__(self):
        pass

    #function to define building code for areas on campus
    def setBuildingCode(self, building):
        if (building == 'El Pomar Center'):
            self.__buildingCode = '12B'
        elif (building == 'Columbine Hall'):
            self.__buildingCode = '15'
        elif (building == 'Centennial Hall'):
            self.__buildingCode = '10'
        elif (building == 'Dwire Hall'):
            self.__buildingCode = '09'
        elif (building == 'Engineering & Applied Science'):
            self.__buildingCode = '14'
        elif (building == 'HYBL Sports Med Perf Ctr'):
            self.__buildingCode = '255'
        elif (building == 'Lane Center'):
            self.__buildingCode = '250'
        elif (building == 'Osborne Center'):
            self.__buildingCode = '32'
        elif (building == 'University Hall'):
            self.__buildingCode = '70'
        elif (building == 'Academic Office Building'):
            self.__buildingCode = '20'
        elif (building == 'Cragmor Hall'):
            self.__buildingCode = '7'
        elif (building == 'Breckenridge House'):
            self.__buildingCode = '25'
        elif (building == 'Cucharas House'):
            self.__buildingCode = '145'
        elif (building == 'UCCS Downtown'):
            self.__buildingCode = '102'
        elif (building == 'University Center'):
            self.__buildingCode = '11-12A'

    def getBuildingCode(self):
        return self.__buildingCode

    def getLocationID(self):
        return f"{self.getBuildingCode()}-{self.getAreaNum()}"

    #encapsulated fields
    def getAssetTag(self):
        return self.__assetTag

    def setAssetTag(self, assetTag):
        self.__assetTag = assetTag

    def getFacility(self):
        return self.__facility

    def setFacility(self, facility):
        self.__facility = facility

    def getBuilding(self):
        return self.__building

    def setBuilding(self, building):
        self.__building = building
        self.setBuildingCode(building)
        
    def getAreaNum(self):
        return self.__areaNum

    def setAreaNum(self, areaNum):
        self.__areaNum = areaNum

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    def getManufacturer(self):
        return self.__manufacturer

    def setManufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def getModelNum(self):
        return self.__modelNum

    def setModelNum(self, modelNum):
        self.__modelNum = modelNum

    def getSerialNum(self):
        return self.__serialNum

    def setSerialNum(self, serialNum):
        self.__serialNum = serialNum

    def getInventoryDate(self):
        return self.__inventoryDate

    def setInventoryDate(self, date):
        self.__inventoryDate = date

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity
    
    def getWarrantyDate(self):
        return self.__warrantyDate

    def setWarrantyDate(self, warrantyDate):
        self.__warrantyDate = warrantyDate
    
    def getUserAssignedTo(self):
        return self.__userAssigned

    def setUserAssignedTo(self, userAssigned):
        self.__userAssigned = userAssigned
    
    def getComment(self):
        return self.__comment

    def setComment(self, comment):
        self.__comment = comment