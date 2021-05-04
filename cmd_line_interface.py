import csv

filename = 'test_driver.csv'

data = []
varContainer = []
x = 1
instrumentList = [1,2,3,4,5]
varFormat = ["VarName", "VarDescription", "Category", "SubCategory", "SubCategory2", "Instrumentation", "VarDataType", "VarData"]
#add options for dataType (continous/categorical) && enter categories for cvategorical || o=1, 1=yes || iterate through x values in range(x)
#add hotkeys
#csv dict to preserve new cat && generate "other" umbrella for faster observation


#email them to verify dict list && kaylee to then list && joy


dataKey = {"cat1":["sub1", "sub2", "sub3"] , 
        "cat2" : ["sub4", "sub5", "sub6"] , 
        "cat3": ["sub7", 
            {"sub8": ["a", "b","c"]}]
}


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

#while loop && save func()
with open(filename, 'r') as csvfile:
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
                description = input() 

        # CATEGORY
        print("The available categories are as follows:\n", dataKey.keys())
        print("Select a default category or enter a custom category")
        category = input()


        # SUBCATEGORY_1
        if category not in dataKey.keys():
            print("is there a subcategory, if so input it. else enter 0")
            sub1 = input()
        else:
            print("Select a subcategory, or enter a new one:", dataKey[category])  
            sub1 = input()  

        # SUBCATEGORY_2
        print("would you like to add a second subcategory  [y/n] ?")
        i = input()
        if(isinstance(sub1,dict)) :
            print("select a second subcategory", dataKey[sub1])
            sub2 = input()
        elif i =='y':
            print("enter a second subcategory:")
            sub2 = input()
        else:
            sub2 = 0
                        
        # INSTRUMENTATION
        print("was instrumentaion used [y/n]")
        i = input()
        if i == 'y':
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


# data to be written row-wise in csv file

  
# opening the csv file in 'a+' mode
file = open('test.csv', 'a+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(data)