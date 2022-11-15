import gc
# Row of Main data table
class MainData:
    def __init__(self,Name,Type,TM,Extends,Implements,ref=None):
        self.Name=Name
        self.Type=Type
        self.TM=TM
        self.Extends=Extends
        self.Implements=Implements
        self.ref=ref
        self.Scope=0

# Each class has its own table with multiple rows
class MainDataTable:
    def __init__(self,List):
        # list of MainData
        self.table=List

    def get_Table(self):
        return self.table

# Row of Class data table
class ClassData:
    def __init__(self,Name,Type,AM,Static,Final):
        self.Name=Name
        self.Type=Type
        self.AM=AM
        self.Static=Static
        self.Final=Final
        self.Scope=0

# Each class has its own table with multiple rows
class ClassDataTable:
    def __init__(self,ClassName,List):
        self.ClassName=ClassName
        # list of ClassData
        self.openedScope=0
        self.ClosedScope=0
        self.table=List

    def get_Table(self):
        return self.table

# Row of Function data table 
class FunctionData:
    def __init__(self,Name,Type,Scope,Final):
        self.Name=Name
        self.Type=Type
        self.Scope=Scope
        self.Final=Final
        self.Scope=0

# Each Function has its own table with multiple rows
class FunctionDataTable:
    def __init__(self,FunctionName,List):
        self.FunctionName=FunctionName
        # list of FunctionData
        self.openedScope=0
        self.ClosedScope=0
        self.table=List

    def get_Table(self):
        return self.table

# retruns mdt obj
def get_MDT_obj():
    for obj in gc.get_objects():
        if isinstance(obj, MainDataTable):
            return obj
    return None

# returns list of all object created
def get_CDT_obj(classname):
    for obj in gc.get_objects():
        if isinstance(obj, ClassDataTable):
            if obj.ClassName==classname:
                return obj
    return None

# # returns list of all object created
# def get_FDT_obj(functionName):
#     _instance=[]
#     for obj in gc.get_objects():
#         if isinstance(obj, FunctionDataTable):
#             if obj.FunctionName==functionName
#                 return obj
#     return None

# looks in main table return false if not found
def lookUpMT(Name,Type):
    obj = get_MDT_obj()
    # looping all rows in mdt
    for i in obj.table:
        if i.Type==Type and i.Name==Name and i.Scope==Scope:
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
    return False , None

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
        if i.Type=="function" and i.Name==FunctionName:
            return True
    return False

# looks  Function data table in MDT return false if not found , and ref of obj if found 
# Looks if Fdt exists or not 
def lookUpFDT_in_CDT(FunctionName,ClassName):
    obj= get_CDT_obj(ClassName)
    if obj != None:
        for i in obj.table:
            if i.Type=="function" and i.Name==FunctionName:
                return True
    return False

# insert into Main table returns false in alraedy exists
def insertMT(Name,Type,TM,Extends,Implements):
    if lookUpMT(Name,Type)==False:
        if Type=="Class":
            res, obj = insertCDT(Name)
            if res:
                # passing obj ref after inserting in class table
                obj = get_MDT_obj()
                data = MainData(Name,Type,TM,Extends,Implements,obj)
                obj.table.append(data)
                return True , obj
            return False
        else:
            res, obj = insertFDT_in_MDT(Name)
            if res:
                # passing obj ref after inserting in class table
                obj = get_MDT_obj()
                data = MainData(Name,Type,TM,Extends,Implements,AM,Static,Final,obj)
                obj.table.append(data)
                return True , obj
            return False
    else:
        return False

# insert into Class table returns false in alraedy exists (checks both the class and if exists then its data )
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
def insertFDT_in_CDT(FunctionName):
    res = lookUpFDT_in_CDT(FunctionName)
    if res == False:
        obj = FunctionDataTable(FunctionName,[])
        return True, obj
    else:
        return False , None

# insert into Function table returns false in alraedy exists
# agr milgya tu true or object wrna false + None
def insertFDT_in_MDT(FunctionName):
    res = lookUpFDT_in_MDT(FunctionName)
    if res == False:
        obj = FunctionDataTable(FunctionName,[])
        return True, obj
    else:
        return False , None

def insert_CD_in_CDT(CDT_Obj, Name, Type, AM, Static, Final):
    obj = ClassData(Name,Type,AM,Static,Final)
    CDT_Obj.table.append(obj)

def insert_FD_in_FDT(FDT_Obj, Name, Type, Scope, Final):
    obj = FunctionData(Name,Type,Scope,Final)
    FDT_Obj.table.append(FDT_Obj)


# Note : check krnay k baad index plus huga 
import json
class SA:
    def __init__(self, TokenSet):
        self.TokenSet = TokenSet
        self.index = 0
        self.errors=[]

    def validate(self):
        if (self.TokenSet[self.index][1]=="@"):
            return True
        return False

    # ======================  Synatx funtions 
    def CM(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["CM"].split("?")
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True , self.TokenSet[self.index - 1]
        else:
            self.index=last_index
            return False , None

    # ===================== INH IMP
    def INH_IMP(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INH_IMP"].split("?")
        if self.TokenSet[self.index][1]=="extends":
            # self.index+=1
            if self.TokenSet[self.index + 1][0]=="Identifier":
                self.index+=2
                return True , [self.TokenSet[self.index - 2],self.TokenSet[self.index - 1]]
            else
                self.errors("Expected Identifier")
                return False , None
        elif self.TokenSet[self.index][1]=="Implements":
            # self.index+=1
            if self.TokenSet[self.index + 1][0]=="Identifier":
                self.index+=2
                return True , [self.TokenSet[self.index - 2],self.TokenSet[self.index - 1]]
            else
                self.errors("Expected Identifier")
                return False , None
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True , self.TokenSet[self.index - 1]
        else:
            self.index = last_index
            return False , None

    # ========================================    neechay wala abhi nhi hua hai    =====================================
    def cb(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["CB"].split("?")    
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
            # return list of cd
            return True    
        res1, attributeObj = self.attribute()                                              
        if res1:
            # add cd element to the list of this fn
            self.cb()
        res2, Fn_def = self.Fn_def()
        elif res2:
            # add cd element to the list of this fn
            self.cb()
        elif self.TokenSet[self.index][1] in arr:
            # add cd element to the list of this fn
            self.index+=1
            # return list of cd
            return True
        else:
            self.index=last_index
            return False

    # =======================================      
    def attribute(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ATTRIBUTE"].split("?")
        res , obj = self.Dec()      
        if res:
            return True , obj
        res2 , obj = self.assign_st()
        if res2:
            return True , obj
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True , self.TokenSet[self.index - 1]
        else:
            self.index=last_index
            self.errors.append("Invalid Attribute  at Line # {}".format(self.TokenSet[self.index][2]))
            return False , None

    # have to cop its sub functions 
    # ===================================================
    def Dec(self):
        last_index=self.index
        obj_list=[]
        res, dtObj= self.dt()
        if res:
            obj_list.append(dtObj)
            if self.TokenSet[self.index][0]=="Identifier":
                obj_list.append(self.TokenSet[self.index][0])
                self.index+=1
                res2, Init_obj= self.INIT()
                if res2:
                    obj_list.append(Init_obj)
                    res3, ListObj = self.List()
                    if res3:
                        obj_list.append(ListObj)
                        return True , obj_list
        self.index=last_index
        # self.errors.append("Invalid Declaration Operator at Line # {}".format(self.TokenSet[self.index][2]))
        return False , None

    # have to cop its sub functions 
    # =========================================
    def assign_st(self):
        last_index=self.index
        assign_list=[]
        res, obj = self.this()
        if res:
            assign_list.append(obj)
            if self.TokenSet[self.index][0]=="Identifier":
                assign_list.append(self.TokenSet[self.index])
                self.index+=1
                res2, x1_Obj = self.x1()         
                if res2:
                    assign_list.append(x1_Obj)
                    res3, init_obj = self.INIT()
                    if res3:
                        assign_list.append(init_obj)
                        res4, ListObj = self.LIST()
                        if res4:
                            assign_list.append(ListObj)
                            return True , assign_list
        self.index=last_index
        # self.errors.append("Invalid Assignment  at Line # {}".format(self.TokenSet[self.index][2]))
        return False , None

    # ==============================================
    def INIT(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INIT"].split("?")
        init_list=[]
        # print(self.TokenSet[self.index][1])
        if self.TokenSet[self.index][1]=="=":   
            init_list.append(self.TokenSet[self.index][1])
            self.index+=1
            res, OE_obj =self.OE()
            if res:
                init_list.append(OE_obj)
                return True , init_list
            self.index=last_index
            return False 
        elif self.TokenSet[self.index][1] in arr:
            init_list.append(self.TokenSet[self.index])
            self.index+=1
            return  True , init_list
        else:
            self.index = last_index
            self.errors.append("Invalid Init at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    # ==============================================
    def LIST(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1]==";":   
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        elif self.TokenSet[self.index][1]==",":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.INIT()
                if res:
                    List.append(obj)
                    res2, obj = self.List()
                    if res2:
                        List.append(obj)
                        return True , List
            self.index=last_index
            return False , None
        else:
            self.index=last_index
            self.errors.append("Invalid List Operator at Line # {}".format(self.TokenSet[self.index][2]))
            return False , None

    # ===================================================
    def x1(self):
        last_index=self.index
        List = []
        if self.TokenSet[self.index][1]==".":
            List.append(self.TokenSet[self.index])
            self.index+=1    
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res , Obj = self.x()
                if res:
                    List.append(obj)
                    return True , List
            last_index=self.index
            return False
        elif self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res , obj = self.const()    
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1]=="]":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        List.append(self.TokenSet[self.index])
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            List.append(self.TokenSet[self.index])
                            self.index+=1    
                            res2, obj2 = self.x()
                            if res2:
                                List.append(obj2)
                                return True , List
            last_index=self.index
            return False
        elif self.TokenSet[self.index][1]=="(":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.parameter()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1]==")":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        List.append(self.TokenSet[self.index])
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            List.append(self.TokenSet[self.index])
                            self.index+=1 
                            res2 , obj2 = self.x()
                            if res2:
                                List.append(obj2)
                                return True , List
            self.index=last_index
            return False
        else:
            self.index=last_index
            return False

    # ============================================================
    def x(self):
        last_index=self.index
        List= []
        if self.TokenSet[self.index][1]==".":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1    
                res , obj = self.x()
                if res:
                    List.append(obj)
                    return True , List
            self.index=last_index
            return False
        self.index=last_index
        res, obj = self.assign_opt()
        if res:
            List.append(obj)
            res, obj = self.OE()
            if res:
                List.append(obj)
                return True , List
            self.index=last_index
            return False

        self.index=last_index
        if self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1    
            res, obj = self.const()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1]=="]":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        List.append(self.TokenSet[self.index])
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            List.append(self.TokenSet[self.index])
                            self.index+=1   
                            res2, obj2 = self.x()
                            if res2:
                                List.append(obj)
                                return True, List
            self.index=last_index
            return False
            
        self.index=last_index
        if self.TokenSet[self.index][1]=="(":
            List.append(self.TokenSet[self.index])
            self.index+=1    
            res , obj = self.parameter()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1]==")":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        List.append(self.TokenSet[self.index])
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            List.append(self.TokenSet[self.index])
                            self.index+=1    
                            res2, obj2 = self.x()
                            if res2:
                                List.append(obj)
                                return True , List
            self.index = last_index
            return False
                    
        self.index=last_index
        res, obj = self.inc_dec()
        if res:
            List.append(obj)
            return True
        self.index=last_index
        return False

    #======================================================
    def this(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["this"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]=="this":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]==".":
                List.append(self.TokenSet[self.index])
                self.index+=1
                return True , List
            self.index= last_index
            return False
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        self.index=last_index
        # self.errors.append("Invalid This statement at Line # {}".format(self.TokenSet[self.index][2]))        
        return False

# =======================================
    def OE(self):
        last_index = self.index
        List=[]
        res, obj = self.AE()
        if res:
            List.append(obj)
            res2, obj2 = self.OE2()
            if res2:
                List.append(obj2)
                return True , List
        self.index=last_index
        return False
     
# ======================================
    def OE2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["OE2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]=="|":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]=="|":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.AE()
                if res:
                    List.append(obj)
                    res2, obj2 = OE2()
                    if res2:
                        List.append(obj2)
                        return True , List
            self.index=last_index
            return False            
        elif self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.index=last_index
            return False
    
# ==============================================================
    def AE(self):
        last_index=self.index
        List=[]
        res, obj = self.RE()
        if res:
            List.append(obj)
            res2, obj2 = self.AE2()
            if res2:
                List.append(obj2)
                return True, List
            self.index= last_index
            return False
        else:
            return False
    
# =======================================================
    def AE2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AE2"].split("?")  
        if self.TokenSet[self.index][1]=="&":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]=="&":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res , obj = self.RE()        
                if res:
                    List.append(obj)
                    res2, obj2 = self.AE2()
                    if res2:
                        List.append(obj2)
                        return True, List
            self.index = last_index
            return False
        elif self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        else:
            self.index=last_index
            return False

# ===========================================
    def RE(self):
        last_index = self.index
        List=[]
        res, obj = self.E()
        if res:
            List.append(obj)
            res2, obj2 = self.RE2()
            if res2:
                List.append(obj2)
                return True , List
            self.index = last_index
            return False
        self.index = last_index
        return False

#===========================================
    def RE2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        arr1=data["RE2"].split("?")  
        List = []
        last_index = self.index
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1    
            res , obj             
            if res:     
                List.append(obj)
                res2, obj2 = self.RE2()
                if res2:
                    List.append(obj2)
                    return True , List
        elif self.TokenSet[self.index][1] in arr1:
            List.append(self.TokenSet[self.index])
            self.index+=1                 
            return True, List
        else:
            return False

# ==========================
    def E(self):
        List = []
        last_index = self.index
        res , obj = self.T()
        if res:
            List.append(obj)
            res2 , obj2 = self.E2()
            if res2:    
                List.append(obj2)
                return True , List
            self.index = last_index
            return False
        else:
            return False
    
# ==================================================
    def E2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PM"].split("?")
        arr1=data["E2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.T()
            if self.T():
                if self.E2(): 
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

# ======================================
    def T(self):
        last_index=self.index
        List=[]
        res, obj = self.F()
        if res:     
            List.append(obj)
            res2, obj = self.T2()
            if res2: 
                List.append(obj2)
                return True , List
            return False
        else:
            return False
    
# ===========================================
    def T2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MDM"].split("?")
        arr1=data["T2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.F()
            if res:
                List.append(obj)
                res2, obj2 = self.T2()
                if res2:
                    List.append(obj2)
                    return True, List
            self.index=last_index
            return False
        elif self.TokenSet[self.index][1] in arr1:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        else:
            self.index=last_index
            return False

    def F(self):
        List=[]
        last_index=self.index
        res, obj = self.this()
        if res:
            List.append(obj)
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res2, obj = self.F2()
                if res2: 
                    List.append(obj)
                    return True
            self.index= last_index
            return False
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res , obj = self.OE() 
            if res:
                List.append(obj)
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    List.append(self.TokenSet[self.index])
                    return True , List
            self.index = last_index
            return False
        if self.TokenSet[self.index][1]=="!":
            List.append(self.TokenSet[self.index])
            res2, obj = self.F()
            if res2:
                List.append(obj)
                return True , List
            self.index= last_index
            return False
        self.index= last_index
        res2, obj = self.inc_dec()
        if res2:
            List.append(obj)
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                return True, List
            return False 
        self.index=last_index
        return False   
    
    def F2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["F2"].split("?") 
        List=[]
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.PL()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    return True
            self.index = last_index
            return False
        self.index = last_index
        res, obj = self.inc_dec()
        if res:
            List.append(obj)
            return True , List
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        self.index=last_index
        return False
    
    def PL(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL"].split("?")  
        last_index = self.index
        res, obj = self.OE()
        List= []
        if res:
            List.append(obj)
            res,obj = self.PL2()
            if res:
                List.append(obj)
                return True, List
            self.index = last_index
            return False
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        self.index = last_index
        return False 

    def PL2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1
            if self.OE():
                if self.PL2():
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False



    def Fn_def(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="def":   
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                    self.index+=1
                    if self.parameter():
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            self.index+=1
                            if self.TokenSet[self.index][1]==":":   
                                self.index+=1
                                if self.Rt():
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                        self.index+=1
                                        if self.MST():
                                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                self.index+=1
                                                return True
        self.index=last_index
        # self.errors.append("Invalid Function Defination Line # {}".format(self.TokenSet[self.index][2]))
        return False



    # Cd K objects bananay hain aur CDT mai append krwanay hain MDT mai bhi 
    # cfgs walay fns mai say is fn mai value pass krni hugii to make CDT obj 
    # ===================
    def Class(self):
        res, CM_Token = self.CM()
        if res:
            # add cm token in cdt
            pass
        if self.TokenSet[self.index][1] == "Class":
            self.index+=1
        res,obj = insertCDT(self.TokenSet[self.index][1])
        if res == True:
            self.index+=1
            res2, INH_IMP_Token = self.INH_IMP()
            if res2:
                # add inh token in cdt
                pass
            if self.TokenSet[self.index][1] == "open":
                obj.openedScope+=1
                self.index+=1
            else:
                self.errors.append("Opening Bracket Not Found")
            res3, cb_token_list = self.cb() 
            if res3:
                # add cb token list in cdt
                pass
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                self.index+=1
                return True
            else:
                self.errors.append("Closing Bracket Not Found")
        else:
            self.errors.append("Class Already Exists")

a = open(r'token.txt','r')
x=a.read().split("?")
arr=[]

for i in x:
    string_without_brackets = i.strip("()")
    arr.append(string_without_brackets.split(","))
print(arr)

obj = SA(arr)
print("Token Validation : " ,obj.validate(),"  ,Current Token IS : ", obj.TokenSet[obj.index], ",  Index IS : ", obj.index)
for errors in obj.errors:
    print(errors )

# rulees : check krwaoo baad mai index mai +1 krwaoo , hr cfg ka fn object return krega
# hr cfg ka fn token ki list retrun krega and then we add this in our cdt
# sb say pehlay return ka dekhra hn ======== laga dunga fn k upr 
# phr cd mai add ka dekhunga hr cfg keliye
# cb kay fn dekhnay prayngay 
# cdt mai add krwatay wqt dekhunga k list return kr ra hai object ya sirf aik object hr function keliye 
# ju ju fn list return kr re hain wo jhn jhn call huray hain aik baar dekhlo