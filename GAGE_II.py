#IMPORT statements
import csv
import pandas as pd
import math
import numpy as np

#PREVIOS neccessary class and method declarations
class Variable:
        def __init__(self, VarName, VarDescription, Category, SubCategory, SubCategory2, Instrumentation, VarDataType, VarData):
            self.Varname = VarName
            self.VarDescription = VarDescription
            self.Category = Category
            self.SubCategory = SubCategory
            self.SubCategory2 = SubCategory2
            self.Instrumentation = Instrumentation
            self.VarDataType = VarDataType
            self.VarData = VarData
        def returnVals(self):
            data = [  self.Varname,self.VarDescription,self.Category,self.SubCategory ,self.SubCategory2 ,self.Instrumentation,self.VarDataType, self.VarData ]
            return data

data = []
varContainer = []
x = 1
varFormat = ["VarName", "VarDescription", "Category", "SubCategory", "SubCategory2", "Instrumentation", "VarDataType", "VarData"]

#FILL and mapping methods
filename = "GAGE-DD_Automation_051921.xlsx - Sheet1.csv"
filename2 = 'test_driver.csv'

def fill_dictionary(FILENAME, collumnNum):
    col_list = ["Domain","Category B","Category C","filler","Instruments"] #ENSURE THESE VALUSE ARE CONSISTENT WITH CSV FILE
    df = pd.read_csv(FILENAME, usecols=col_list)
    return df[col_list[collumnNum-1]]

def filterCells(df):
    dict1 = {}
    j = 0
    for i in df:
        j+=1
        if str(i) != "nan":
            dict1[i] = j
    return dict1

def findSubCategories(dictionary, nxtDict, category):
    arr1 = []
    arr2 = []
    val1 = dictionary[category]
    for i in dictionary: 
        if dictionary[i] > val1: 
            arr1.append(i)
    val2 = dictionary[min(arr1)]

    for j in nxtDict:
        if nxtDict[j] > val1 and nxtDict[j] < val2: 
            arr2.append(j)

def printHotkeys(arrayList): # add hotley arrays to each
    n = 0
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    print(hotkeyDict)

def returnHotkeys(num, arrayList):
    n = 0
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    v = list(arrayList.keys())
    return v[num]
#Execute methods on csv
df_categories = filterCells(fill_dictionary(filename,1 ))
df_subCategories = filterCells(fill_dictionary(filename,2 ))
df_subSubCategories = filterCells(fill_dictionary(filename,3 ))
df_instruments = filterCells(fill_dictionary(filename,5 ))

#print(findSubCategories(df_categories,df_subCategories, 'Lifetime Pharmacological Treatment'))

printHotkeys(df_categories)


#LOOP logic
with open(filename2, 'r') as csvfile:
    datareader = csv.reader(csvfile)


    for row in datareader:

        # NAME
        name = row[0]
        description = row[1]
        print("\n now dealing with variable :", name)

        # DESCRIPTION
        if  len(row[1]) == 1: 
            print("No description, would you like to add one [y/n] ?")
            i = input()
            if i == 'y':
                print("enter description")
                description = input()
        else: 
            print("The description is:", row[1])
            print("would you like to change it [y/n] ?")
            i = input()
            if i == 'y':
                print("enter description:")
                description = (input()) 

        # CATEGORY
        print("The available categories are as follows:\n")
        printHotkeys(df_categories)
        print("Select a default category or enter a custom category")
        category = input()
        category = str(returnHotkeys(int(category), df_categories))
        #ADD OPTION FOR MISC!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        
        subCat1 = findSubCategories(df_categories, df_subCategories, category)
        print("n", subCat1)
        print("Select a subcategory, or enter a new one:")  
        printHotkeys(subCat1)
        sub1 = returnHotkeys(input(), subCat1)

        # SUBCATEGORY_2
        subCat2 = findSubCategories(df_subCategories, df_subSubCategories, sub1)
        print("would you like to add a second subcategory  [y/n] ?")
        i = input()
        if(isinstance(sub1,dict)) :
            print("select a second subcategory")
            printHotkeys(subCat2)
            sub2 = returnHotkeys(input(), subCat2)
        elif i =='y':
            print("enter a second subcategory:")
            sub2 = input()
        else:
            sub2 = 0
                        
        # INSTRUMENTATION

        print("was instrumentaion used [y/n]")
        i = input()
        if i == 'y':
            instrumentList = findSubCategories(category, df_instruments)
            print("Select from the following list or enter your own:", instrumentList)
            instrument = input()
            print(" would you like to enter any information regarding the methodology of the data collection [y/n] ?")
            i = input()
            if i =='y': 
                print("enter:")
                i = input()
                instrument = instrument + ":" + i
        else: instrument = 0

        # VARIABLE TYPE
        print("what kind of data is stored in this varibale ?")
        varType = input()

        #VARIABLE DATA
        print("would you like to add any specifics about the data stored ?")
        varData = input()

        #ENTER DATA
        varObject =  Variable(name, description, category, sub1, sub2, instrument, varType, varData)
        varContainer = varObject.returnVals()
        data.append(varContainer)

        #BREAK
        print("save & quit ? y/n")
        breakVar = input()
        if breakVar == "y": break

  
# opening the csv file in 'a+' mode
file = open('test.csv', 'a+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(data)