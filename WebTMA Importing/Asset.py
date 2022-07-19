#This class describes an asset object to be imported into WebTMA
#Author: Caleb Harris - UCCS OIT Services Professional
#Date Created: 4/8/2022

from distutils.command.build import build
from pickle import TRUE
from re import sub


class Asset:
    '''
    This class will define an Asset object
    '''
    #constructor
    def __init__(self):

        #initialize variables for asset object
        #fields
        self.__assetTag = None
        self.__facility = None
        self.__quantity = None
        self.__building = None
        self.__buildingCode = None
        self.__areaNum = None
        self.__description = None
        self.__type = None
        self.__manufacturer = None
        self.__modelNum = None
        self.__serialNum = None
        self.__warrantyDate = None
        self.__userAssigned = None
        self.__comment = None
        self.__subtype = None
        
        #field boolean values
        self.__hasAssetTag = False
        self.__hasFacility = False
        self.__hasQuantity = False
        self.__hasBuilding = False
        self.__hasBuildingCode = False
        self.__hasAreaNum = False
        self.__hasDescription = False
        self.__hasType = False
        self.__hasManufacturer = False
        self.__hasModelNum = False
        self.__hasSerialNum = False
        self.__hasWarrantyDate = False
        self.__hasUserAssignedTo = False
        self.__hasComment = False
        self.__hasSubtype = False

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
        elif (building == 'Cybersecurity'):
            self.__buildingCode = '3650'

    def getBuildingCode(self):
        return self.__buildingCode

    def getLocationID(self):
        return f"{self.getBuildingCode()}-{self.getAreaNum()}"

    #encapsulated fields
    def getAssetTag(self):
        return self.__assetTag

    def setAssetTag(self, assetTag):
        self.__hasAssetTag = True
        self.__assetTag = assetTag

    def hasAssetTag(self):
        return self.__hasAssetTag

    def getFacility(self):
        return self.__facility

    def setFacility(self, facility):
        self.__hasFacility = True
        self.__facility = facility

    def hasFacility(self):
        return self.__hasFacility

    def getBuilding(self):
        return self.__building

    def setBuilding(self, building):
        self.__hasBuilding = True
        self.__hasBuildingCode = True
        self.__building = building
        self.setBuildingCode(building)

    def hasBuilding(self):
        return self.__hasBuilding

    def hasBuildingCode(self):
        return self.__hasBuildingCode
        
    def getAreaNum(self):
        return self.__areaNum

    def setAreaNum(self, areaNum):
        self.__hasAreaNum = True
        self.__areaNum = areaNum

    def hasAreaNum(self):
        return self.__hasAreaNum

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__hasDescription = True
        self.__description = description

    def hasDescription(self):
        return self.__hasDescription

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__hasType = True
        self.__type = type

    def hasType(self):
        return self.__hasType

    def getManufacturer(self):
        return self.__manufacturer

    def setManufacturer(self, manufacturer):
        self.__hasManufacturer = True
        self.__manufacturer = manufacturer

    def hasManufacturer(self):
        return self.__hasManufacturer

    def getModelNum(self):
        return self.__modelNum

    def setModelNum(self, modelNum):
        self.__hasModelNum = True
        self.__modelNum = modelNum

    def hasModelNum(self):
        return self.__hasModelNum

    def getSerialNum(self):
        return self.__serialNum

    def setSerialNum(self, serialNum):
        self.__hasSerialNum = True
        self.__serialNum = serialNum

    def hasSerialNum(self):
        return self.__hasSerialNum

    def getInventoryDate(self):
        return self.__inventoryDate

    def setInventoryDate(self, date):
        self.__hasInventoryDate = True
        self.__inventoryDate = date

    def hasInventoryDate(self):
        return self.__hasInventoryDate

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__hasQuantity = True
        self.__quantity = quantity

    def hasQuantity(self):
        return self.__hasQuantity
    
    def getWarrantyDate(self):
        return self.__warrantyDate

    def setWarrantyDate(self, warrantyDate):
        self.__hasWarrantyDate = True
        self.__warrantyDate = warrantyDate

    def hasWarrantyDate(self):
        return self.__hasWarrantyDate
    
    def getUserAssignedTo(self):
        return self.__userAssigned

    def setUserAssignedTo(self, userAssigned):
        self.__hasUserAssignedTo = True
        self.__userAssigned = userAssigned

    def hasUserAssignedTo(self):
        return self.__hasUserAssignedTo
    
    def getComment(self):
        return self.__comment

    def setComment(self, comment):
        self.__hasComment = True
        self.__comment = comment

    def hasComment(self):
        return self.__hasComment

    def getSubtype(self):
        return self.__subtype
    
    def setSubtype(self, subtype):
        self.__hasSubtype = True
        self.__subtype = subtype

    def hasSubtype(self):
        return self.__hasSubtype
    
