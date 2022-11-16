import gc
# Row of Main data table
class MainData:
    instances = []
    def __init__(self,Name,Type,TM,Extends,Implements,ref=None):
        self.Name=Name
        self.Type=Type
        self.TM=TM
        self.Extends=Extends
        self.Implements=Implements
        self.ref=ref
        self.Scope=0
        self.__class__.instances.append(self)


# Each class has its own table with multiple rows
class MainDataTable:
    instances = []
    def __init__(self,List):
        # list of MainData
        self.table=List
        self.__class__.instances.append(self)
        self.ScopeNumber=0


    def get_Table(self):
        return self.table

# Row of Class data table
class ClassData:
    instances = []
    def __init__(self,Name,Type,AM,Static,ref=None,Scope=0):
        self.Name=Name
        self.Type=Type
        self.AM=AM
        self.Static=Static
        self.ref=ref
        self.__class__.instances.append(self)

# Each class has its own table with multiple rows
class ClassDataTable:
    instances = []
    def __init__(self,ClassName,List):    
        self.ClassName=ClassName
        # list of ClassData
        self.ScopeNumber=0
        self.table=List
        self.__class__.instances.append(self)

    def get_Table(self):
        return self.table

# Row of Function data table 
class FunctionData:
    instances = []
    def __init__(self,Name,Type,Scope=0):
        self.Name=Name
        self.Type=Type
        self.Scope=Scope
        self.__class__.instances.append(self)

# Each Function has its own table with multiple rows
class FunctionDataTable:
    instances = []
    def __init__(self,FunctionName,List):
        self.FunctionName=FunctionName
        # list of FunctionData
        self.ScopeNumber=0
        self.table=List
        self.__class__.instances.append(self)

    def get_Table(self):
        return self.table

# retruns mdt obj
def get_MDT_obj():
    for obj in MainDataTable.instances:
        return obj
    return None

# returns list of all object created
def get_CDT_obj(classname):
    for obj in ClassDataTable.instances:
        if obj.ClassName==classname:
            return obj
    return None

# looks in main table return false if not found
def lookUpMT(Name,Type):
    obj = get_MDT_obj()  
    # looping all rows in mdt
    for i in obj.table:
        if i.Type==Type and i.Name==Name :
            return True
    return False

# looks in ClassDataTable return false if not found , and ref of obj if found 
# looks for class data we have to give classname
def lookUpCD_in_CDT(ClassObject,Name,Type,Scope):
    for i in ClassObject.table:
        if i.Type==Type and i.Name==Name and i.Scope==Scope:
            return True
    return False

# looks for class data table return false if not found , and ref of obj if found 
# Looks if cdt exists or not 
def lookUpCDT(ClassName):
    obj = get_CDT_obj(ClassName)
    if obj != None:
        return True
    return False 

# looks in FunctionDataTable return false if not found , and ref of obj if found 
# looks for Function data we have to give functionname
def lookUpFD(FunctionObject,Name,Type):
    for i in FunctionObject.table:
        if i.Type==Type and i.Name==Name and i.Scope==Scope:
            return True
    return False

# looks  Function data table in MDT return false if not found , and ref of obj if found 
# Looks if Fdt exists or not 
def lookUpFDT_in_MDT(FunctionName):
    obj= get_MDT_obj()
    for i in obj.table:
        if i.Type=="def" and i.Name==FunctionName:
            return True
    return False

# looks  Function data table in cDT return false if not found , and ref of obj if found 
# Looks if Fdt exists or not 
def lookUpFDT_in_CDT(FunctionName,ClassName):
    obj= get_CDT_obj(ClassName)
    if obj != None:
        for i in obj.table:
            if i.Type=="def" and i.Name==FunctionName:
                return True
    return False


# insert into Class table returns false if alraedy exists (checks both the class and if exists then its data )
# agr milgya tu true or object wrna false + None
def insertCDT(ClassName):
    res  = lookUpCDT(ClassName)
    if res == False:
        obj = ClassDataTable(ClassName,[])
        return True, obj
    else:
        return False , None


# insert into Function table returns false in alraedy exists
# agr milgya tu true or object wrna false + None
def insertFDT_in_CDT(FunctionName,ClassName):
    res = lookUpFDT_in_CDT(FunctionName,ClassName)
    if res == False:
        # insert krna hai
        obj = FunctionDataTable(FunctionName,[])
        return True, obj
    else:
        return False , None

# insert into Function table returns false in alraedy exists
# agr milgya tu true or object wrna false + None
def insertFDT_in_MDT(FunctionName):
    res = lookUpFDT_in_MDT(FunctionName)
    if res == False:
        # insert krna hai 
        obj = FunctionDataTable(FunctionName,[])
        return True, obj
    else:
        return False , None

#  idvcidual lookup krna hai (inserting row in table)
def insert_CD_in_CDT(CDT_Obj, Name, Type, AM, Static):
    # lookup cd in cdt 
    obj = ClassData(Name,Type,AM,Static)
    CDT_Obj.table.append(obj)

#  idvidual lookup krna hai (inserting row in table)
def insert_FD_in_FDT(FDT_Obj, Name, Type, Scope):

    obj = FunctionData(Name,Type,Scope)
    FDT_Obj.table.append(FDT_Obj)



# Note :token check krnay k baad index plus huga
class SA:
    def __init__(self, TokenSet):
        self.TokenSet = TokenSet
        self.index = 0
        self.errors=[]

    def validate(self):
        if self.s():
            if (self.TokenSet[self.index][1]=="@"):
                return True
        return False
    
    def CompareOp(self,token1,token2,Op):
        return True

    def s(self):
        mdt=MainDataTable([])
        while self.TokenSet[self.index][1]!="@":   
            if self.TokenSet[self.index][1]=="def":
                res, obj = self.insertFunction_inMain()
                if res==False:
                    self.errors.append("")
                    self.errors.append(("Invalid fn at Line # {}").format(self.TokenSet[self.index][2]))
                    return False , None                 
            elif self.TokenSet[self.index][0]=="Class":
                res, obj = self.insertClass()
                if res==False:
                    self.errors.append("")
                    self.errors.append(("Invalid class at  Line # {}").format(self.TokenSet[self.index][2]))
                    return False , None
            else:
                # add in mdt  (self,Name,Type,TM,Extends,Implements,ref=None):
                data = MainData( self.TokenSet[self.index][1], self.TokenSet[self.index][0], None , False , False )
                mdt.table.append(data)
                self.index+=1

        return True


    def insertFunction_inClass(self,ClassObj):
        if self.TokenSet[self.index][1]=="def":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                # insert FDT
                res, FN_obj = insertFDT_in_CDT(self.TokenSet[self.index][1], ClassObj.ClassName)
                self.index+=1

                if res==False:
                    self.errors.append("Function Already Exisits In class")
                    return False , None
                else:
                    #(self,Name,Type,AM,Static,ref=None):
                    data = ClassData(FN_obj.FunctionName,"def", None, False,FN_obj)
                    ClassObj.table.append(data)

                    if  self.TokenSet[self.index][1]=="open":
                        # (self,Name,Type,Scope)
                        # Fn_data = FunctionData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], FN_obj.ScopeNumber)
                        # FN_obj.table.append(Fn_data)

                        self.index+=1
                        FN_obj.ScopeNumber+=1
                        while FN_obj.ScopeNumber !=0 :
                            # open , close , fn , close pr opened scope -=1 huga
                            if  self.TokenSet[self.index][1]=="open":
                                # Fn_data = FunctionData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], FN_obj.ScopeNumber)
                                # FN_obj.table.append(Fn_data)
                                # insert CDT
                                self.index+=1
                                FN_obj.ScopeNumber+=1
                            elif  self.TokenSet[self.index][1]=="close":
                                # Fn_data = FunctionData(self.TokenSet[self.index][1],self.TokenSet[self.index][0],FN_obj.ScopeNumber)
                                # FN_obj.table.append(Fn_data)
                                self.index+=1
                                FN_obj.ScopeNumber-=1
                            else:
                                Fn_data = FunctionData(self.TokenSet[self.index][1],self.TokenSet[self.index][0], FN_obj.ScopeNumber)
                                FN_obj.table.append(Fn_data)
                                self.index+=1
                        return True , FN_obj    
                    return True , FN_obj
            else:
                self.errors.append(("Invalid Def Name Line # {}").format(self.TokenSet[self.index][2]))
                return False, None

    def insertFunction_inMain(self):
        MDT=get_MDT_obj()
        if self.TokenSet[self.index][1]=="def":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                # insert CDT
                res, FN_obj = insertFDT_in_MDT(self.TokenSet[self.index][1])                 
                self.index+=1

                if res==False:
                    self.errors.append("Function Already Exisits In Main")
                    return False , None
                else:
                    # obj add in mdt (self,Name,Type,TM,Extends,Implements,ref=None)
                    data= MainData(FN_obj.FunctionName,"def",False,False,False,FN_obj)
                    MDT.table.append(data)

                    if  self.TokenSet[self.index][1]=="open":
                        # insert FD (self,Name,Type,Scope,Final):
                        # Fn_data = FunctionData(self.TokenSet[self.index][1],self.TokenSet[self.index][0],FN_obj.ScopeNumber)
                        # FN_obj.table.append(Fn_data)
                        self.index+=1
                        FN_obj.ScopeNumber+=1

                        while FN_obj.ScopeNumber !=0 :
                            # open , close , fn , close pr opened scope -=1 huga
                            if  self.TokenSet[self.index][1]=="open":
                                # insert CDT
                                # insert FD (self,Name,Type,Scope,Final):
                                # Fn_data = FunctionData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], obj.ScopeNumber)
                                # FN_obj.table.append(Fn_data)
                                self.index+=1
                                FN_obj.ScopeNumber+=1
                            elif  self.TokenSet[self.index][1]=="close":
                                # insert FD (self,Name,Type,Scope,Final):
                                # Fn_data = FunctionData(self.TokenSet[self.index][1],self.TokenSet[self.index][0], obj.ScopeNumber)
                                # FN_obj.table.append(Fn_data)
                                self.index+=1
                                FN_obj.ScopeNumber-=1
                            else:
                                Fn_data = FunctionData(self.TokenSet[self.index][1],self.TokenSet[self.index][0],obj.ScopeNumber)
                                FN_obj.table.append(Fn_data)
                                self.index+=1

                        return True , FN_obj
                    return True , obj
            else:
                self.errors.append(("Invalid Class Name Line # {}").format(self.TokenSet[self.index][2]))
                return False, None


    def insertClass(self):
        MDT=get_MDT_obj()
        if self.TokenSet[self.index][0]=="Class":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                res, Class_obj = insertCDT(self.TokenSet[self.index][1])
                self.index+=1
                if res==False:
                    self.errors.append("Class Already Exisits ")
                    return False , None
                else:

                    data= MainData(Class_obj.ClassName,"Class",False,False,False,Class_obj)
                    MDT.table.append(data)

                    # extends modifiers maybe there 
                    if self.TokenSet[self.index][1]=="extends":
                        # (self,Name,Type,AM,Static,ref=None)         
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Identifier":
                            
                            #self,Name,Type,TM,Extends,Implements,ref=None,scope
                            data.Extends= True
                            # data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                            # Class_obj.table.append(data)

                            # insert CDT
                            self.index+=1
                        else:
                            self.errors.append(("Invalid Idnetifier at Line # {}").format(self.TokenSet[self.index][2]))
                            return False , None
                    #  Impl modifiers maybe there   
                    if self.TokenSet[self.index][1]=="Implements":
                        data.Implements= True
                        # insert CDT
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Identifier":
                            # insert CDT
                            self.index+=1
                            data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                            Class_obj.table.append(data)
                        else:
                            self.errors.append(("Invalid Idnetifier at Line # {}").format(self.TokenSet[self.index][2]))
                            return False , None
                    if  self.TokenSet[self.index][1]=="open":
                        # insert CDT
                        # data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                        # Class_obj.table.append(data)
                        self.index+=1
                        Class_obj.ScopeNumber+=1
                        while Class_obj.ScopeNumber !=0 :
                            # open , close , fn , close pr opened scope -=1 huga
                            if  self.TokenSet[self.index][1]=="open":
                                # insert CDT
                                # data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                                # Class_obj.table.append(data)
                                self.index+=1
                                Class_obj.ScopeNumber+=1
                            elif  self.TokenSet[self.index][1]=="close":
                                # insert CDT
                                # data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                                # Class_obj.table.append(data)

                                self.index+=1
                                Class_obj.ScopeNumber-=1
                            elif self.TokenSet[self.index][1]=="def":
                                res , FN_obj = self.insertFunction_inClass(Class_obj)
                                if res==False:
                                    self.errors.append(("Invalid fnat Line # {}").format(self.TokenSet[self.index][2]))
                            else:
                                data = ClassData(self.TokenSet[self.index][1], self.TokenSet[self.index][0], False, False, None , Class_obj.ScopeNumber  )
                                Class_obj.table.append(data)
                                self.index+=1
                        
                    return True , obj
            else:
                self.errors.append(("Invalid Class Name Line # {}").format(self.TokenSet[self.index][2]))
                return False, None


a = open(r'token.txt','r')
x=a.read().split("?")
arr=[]


# insert k fns call krwanay hain aur lookup dekhna hai

for i in x:
    string_without_brackets = i.strip("()")
    arr.append(string_without_brackets.split(","))

obj = SA(arr)

print("Validation: ",obj.validate())
