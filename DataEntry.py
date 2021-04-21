#container for csv transfer
varContainer = []
#loop condition
x = 1
# multidimensional dict to contain value, categories & subcategories
dataKey = {"cat1":["sub1", "sub2", "sub3"] , 
        "cat2" : ["sub4", "sub5", "sub6"] , 
        "cat3": ["sub7", 
            {"sub8": ["a", "b","c"]}]
}

#class to store data for csv input
class Variable:
        def __init__(self, VarName, Category, SubCategory, SubCategory2, Instrumentation, VarDataType, VarData):
            self.Varname = VarName
            self.Category = Category
            self.SubCategory = SubCategory
            self.SubCategory2 = SubCategory2
            self.Instrumentation = Instrumentation
            self.VarDataType = VarDataType
            self.VarData = VarData
        def returnVals(self):
            data = [  self.Varname,self.Category,self.SubCategory ,self.SubCategory2 ,self.Instrumentation,self.VarDataType, self.VarData ]
            return data

#driver loop for comand line interface (later tio be connected to GUI)
while(x ==1):

    print("enter var name")   # take variable name from csv file from column && include description
    a1 = input()
    print(dataKey.keys())

    a = input()
    print(dataKey[a])

    b = input()

    #print(type(dataKey[b]))  #delete l8er
    if(isinstance(b,dict)):
        print(dataKey[b])

        c = input()
    else:
        c = 0


#ssee documentation for  lists of instrumentation
    print("Was instrumentation used, if so specify which kind was utilized, else enter 0") # connnect list based on categories (python psuedo switch statement)
    d = input()

# item level vs toatal score || both
# reverse scored scales --- include scoring ?
    print("What kind of data does this variable contain? (Continous / Categorical)")
    e = input()

    print("Enter the data contained by this variable:") # modify to make clearer only appliccable tp categorical && connect
    f = input() 
                    # loop thru num of categories && includes defaults that have common occurences

    
    newVar = Variable(a1,a,b,c,d,e,f)
    varContainer.append(newVar)

    print("press 0 to exit and enter variables, 1 to continue, and 2 to enter")
    x = input()

# enter elenments int csv file

print(varContainer)