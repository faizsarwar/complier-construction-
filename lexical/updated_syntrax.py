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

    def while_st(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1]=="while":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.OE()
                if res:
                    List.append(obj)
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            List.append(self.TokenSet[self.index])
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                List.append(self.TokenSet[self.index])
                                self.index+=1
                                res3, obj3 = self.body()
                                if res3:
                                    List.append(obj3)
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        List.append(self.TokenSet[self.index])
                                        self.index+=1
                                        return True, List
                self.index = last_index
                return False
        self.index=last_index
        self.errors.append("Invalid While Statement Body at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def while_condition(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        List=[]
        res, obj = self.Id_const()
        if res:
            List.append(obj)
            if self.TokenSet[self.index][1] in arr:
                List.append(self.TokenSet[self.index])
                self.index+=1
                res2, obj2 = self.Id_const()
                if res2:
                    List.append(obj2)
                    return True, List
            self.index = last_index
            return False , []
        else:
            self.index=last_index
            self.errors.append("Invalid While Condition at Line # {}".format(self.TokenSet[self.index][2]))
            return False , []

    def If_condition(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        List=[]
        res, obj = self.Id_const()
        if res:
            List.append(obj)
            if self.TokenSet[self.index][1] in arr:
                List.append(self.TokenSet[self.index])
                self.index+=1
                res2, obj2 = self.Id_const()
                if res2:
                    return True, List
            self.index = last_index
            return False, []
        else:
            self.index=last_index
            self.errors.append("Invalid If Condition at Line # {}".format(self.TokenSet[self.index][2]))
            return False, []

    def Id_const(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][0]=="Identifier":
            List.append(self.TokenSet[self.index])
            self.index+=1        
            return True, List
        res, obj = self.const()
        if res:
            List.append(obj)
            return True, List
        self.index=last_index
        self.errors.append("Invalid Identifier or constant at Line # {}".format(self.TokenSet[self.index][2]))
        return False, []


    def const(const):
        last_index=self.index
        Float_regex = '[+-]?[0-9]+\.[0-9]+'
        Int_regex='[+-]?[0-9]+'
        List=[]
        if(re.search(Float_regex,self.TokenSet[self.index][0])): 
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        elif(re.search(Int_regex,self.TokenSet[self.index][0])): 
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.index=last_index
            self.errors.append("Invalid Const at Line # {}".format(self.TokenSet[self.index][2]))
            return False, []

    def body(self):
        last_index=self.index
        List=[]
        res, obj = self.MST()
        if res:
            List.append(obj)
            return True, List
        self.index=last_index
        self.errors.append("Invalid  Body at Line # {}".format(self.TokenSet[self.index][2]))
        return False, []


    def function_call(self):
        last_index= self.index
        List=[]
        if self.TokenSet[self.index][0]=="Identifier":
            List.append(self.TokenSet[self.index])
            self.index+=1        
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.param_list()
                if res:    
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        List.append(self.TokenSet[self.index])
                        self.index+=1 
                        if self.TokenSet[self.index][1]==";":List.append(self.TokenSet[self.index])
                            self.index+=1 
                            return True, List
            self.index = last_index
            return False
        self.index=last_index
        # self.errors.append("Invalid Function Call at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def param_list(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARAM_LIST"].split("?")  
        List=[]
        if self.TokenSet[self.index][0]=="Identifier":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res2, obj = self.para2()
            if res2:
                List.append(obj)
                return True, List     
        if self.TokenSet[self.index][1] in arr:
                List.append(self.TokenSet[self.index])
                self.index+=1
                return True, List
    
        self.index=last_index
        self.errors.append("Invalid Param List at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def para2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARA_LIST2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]==",":
            List.append(self.TokenSet[self.index])
            self.index+=1 
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.para2()
                if res:
                    List.append(obj)
                    return True, List
            return False,[]
        if self.TokenSet[self.index][1] in arr:
                List.append(self.TokenSet[self.index])
                self.index+=1
                return True
        self.index=last_index
        return False, []

    def k1(slef):
        last_index=self.index
        List=[]
        res, obj = self.Dec()
        if res:
            List.append(obj)
            return True, List

        self.index= last_index
        res2 , obj = self.assign_st()
        if res2:
            return True , Obj
        return False, []

    def k3(self):
        last_index=self.index
        List=[]
        res, obj = self.inc_dec()
        if res:
            List.append(obj)
            res2, obj = self.k()
            if res2:
                List.append(obj)
                return True, List
            self.index = last_index
            return False. []

        self.index = last_index
        res, obj = self.k()
        if res:
            List.append(obj)
            res2, obj2 = self.inc_dec()
            if res2:
                List.append(obj2)
                return True, List
            self.index = last_index
            return False, []
        return False,[]

    def k(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][0]=="Identifier":
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List

        self.index = last_index
        res, obj = self.function_call()
        if res:
            List.append(obj)
            self.index+=1
            return True, List

        self.index = last_index
        res, obj = self.obj()
        if res:
            List.append(obj)
            self.index+=1
            return True, List

        self.index = last_index
        res, obj = self.Array()
        if res:
            List.append(obj)
            self.index+=1
            return True, List

        else:
            return False

    def obj(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][0]=="Identifier":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]==".":
                List.append(self.TokenSet[self.index])
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    self.obj2(List)
            self.index=last_index
            return False, []
        self.index=last_index
        return False, []
    
    def obj2(self,List):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["OBJ2"].split("?")  
        if self.TokenSet[self.index][1]==".":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                self.obj2(List)
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            return False, []

    def inc_dec(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INC_DEC"].split("?")
        List=[]  
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True,List
        else:
            self.index=last_index
            self.errors.append("Invalid Increment Or Decrement Operator at Line # {}".format(self.TokenSet[self.index][2]))
            return False , []

    def interface(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][0]=="Interface":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    res, obj = self.MST()
                    if res:
                        List.append(obj)
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                            List.append(self.TokenSet[self.index])
                            self.index+=1
                            return True, List
            return False, []
        self.index=last_index
        # self.errors.append("Invalid Interface defination Operator at Line # {}".format(self.TokenSet[self.index][2]))
        return False, []

    def dt(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        List=[]
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.errors.append("Invalid Data Type at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def Rt(self):
        last_index=self.index
        List=[]
        res, obj = self.dt()
        if res:
            List.append(obj)
            return True, List

        self.index=last_index
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True

        self.index=last_index
        res, obj = self.dt()
        if res:
            List.append(obj)
            res2 , obj2 = self.Rt1()
            if res2:
                List.append(obj2)
                return True, List

        if self.TokenSet[self.index][1]=="void":
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            return False, []


    def Rt1(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.Rt2()
                if res:
                    List.append(obj)
                    return True, List
            self.index=last_index
            return False            
        self.index=last_index
        return False
    
    def Rt2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.Rt2()
                if res:
                    List.append(obj)
                    return True, List
            self.index= last_index
            return False , []
        elif self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        self.index=last_index
        return False    

    def Error_type(self):
        arr= ['ArithmeticException','ClassNotFoundException','ArrayIndexOutOfBoundsException','SecurityException']
        List=[]
        if self.TokenSet[self.index][1] in arr:
                List.append(self.TokenSet[self.index])
                self.index+=1
                return True, List
        else:
            self.errors.append("Invalid Error Type for Throw statement Operator at Line # {}".format(self.TokenSet[self.index][2]))
            return False, []
    
    
    def assign_opt(self):
        last_index= self.index
        List=[]
        if self.TokenSet[self.index][1]=="=":
            List.append(self.TokenSet[self.index])
            self.index+=1    
            return True, List

        res , obj = self.c_assign()
        if res:
            List.append(obj)
            return True , List
        else:
            self.index = last_index
            self.errors.append("Invalid Assignmengt  Operatoration at Line # {}".format(self.TokenSet[self.index][2]))
            return False, []

    def c_assign(self):
        last_index=self.index
        arr= ["+", "-", "*", "/", "%"]
        List=[]
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1    
            if self.TokenSet[self.index][1]=="=":
                List.append(self.TokenSet[self.index])
                self.index+=1    
                return True, List
            self.index= last_index
            return False
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
            self.index=last_index
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

    #=================================================
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
    
    #==============================================================================
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

    #=================================================
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

#===============================
    def PL2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]==",":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.OE()
            if res:
                List.append(obj)
                res2, obj2 = self.PL2()
                if res2:
                    return True, List
            self.index = last_index
            retrun False
        elif self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        else:
            self.index=last_index
            return False

# ========================================
    def SST(self):
        last_index= self.index
        res1, List1 = self.Obj_dec()
        if res1:
            return True , List1

        self.index = last_index
        res1, List1 = self.Fn_def()
        if res1:          
            return True, List1

        self.index = last_index
        res1, List1 = self.Array()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.switch()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.Class()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.interface()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.interface()
        if self.while_st():
            return True, List

        self.index = last_index
        res1, List1 = self.function_call()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.for_st()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.If_Else()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.Dec()
        if self.Dec():
            return True, List1
        
        self.index = last_index
        res1, List1 = self.assign_st()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.TRY()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.TRY()
        if self.CATCH():
            return True, List1

        self.index = last_index
        res1, List1 = self.FINALLY()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.BREAK()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.THROW()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.CONTINUE()
        if res1:
            return True, List1

        self.index = last_index
        res1, List1 = self.Return()
        if res1:
            return True, List1
        
        self.errors.append("Invalid statment at Line # {}".format(self.TokenSet[self.index][2]))
        return False

# ====================================================
    def Return(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1]=="return":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.case()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1]==";":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    return True, List
            self.index= last_index
            return False
        self.index=last_index
        self.errors.append("Invalid Return Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

# ====================================================    
    def case(self):
        last_index=self.index
        List=[]
        res, obj=self.OE()
        if self.OE():
            LIST.append(obj)
            return True, List    

        self.index=last_index
        if self.TokenSet[self.index][1]=="return":   
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List      
        self.index=last_index
        return False

# ====================================================
    def If_Else(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1]=="if":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.OE()
                if res:
                    List.append(obj)
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        List.append(self.TokenSet[self.index])
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            List.append(self.TokenSet[self.index])
                            self.index+=1
                            if self.body():
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                    List.append(self.TokenSet[self.index])
                                    self.index+=1
                                    res , obj = self.Else()
                                    if res:
                                        return True , List
                self.index=last_index
                return False
        self.index=last_index   
        self.errors.append("Invalid If / Else  at Line # {}".format(self.TokenSet[self.index][2]))        
        return False

#==================================================================    
    def Else(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Else"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]=="else":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.body() 
                if res:
                    List.append(obj)
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        List.append(self.TokenSet[self.index])
                        self.index+=1
                        return True, List
            self.index = last_index
            return False
        elif self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List     
        self.index=last_index      
        self.errors.append("Invalid Else Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False


    def Array(self):
        last_index=self.index
        List = []
        res , obj = self.dt()
        if res:
            List.append(obj)
            if self.TokenSet[self.index][0]=="Identifier":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.A()
                if res:
                    List.append(obj)
                    res, obj = self.B()
                    if res:
                        List.append(obj)
                        res, obj = self.A1()
                        if res:
                            List.append(obj)
                            if self.TokenSet[self.index][1]==";":
                                List.append(self.TokenSet[self.index])
                                return True , List
            self.index=last_index
            return False, 
        self.index=last_index
        # self.errors.append("Invalid Array at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def A(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A"].split("?")  
        List=[]
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        self.index= last_index
        res, obj =  self.A3()
        if res:
            List.append(obj)
            self.index+=1
            return True, List

        self.index=last_index
        return False
    
    def A3(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="]":    
                self.TokenSet[self.index]   
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
                    self.TokenSet[self.index]
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="]":    
                        self.TokenSet[self.index]   
                        self.index+=1 
                        return True, List
            self.index = last_index
            return False
        self.index = last_index
        return False

    def A1(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A1"].split("?")  
        List=[]
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.array_list1()
            if res:
                List.append(obj)
                return True, List
            self.index = last_index
            return False
        elif self.TokenSet[self.index][1] in arr :
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.index=last_index
            return False

    def B(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["B"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]=="=":  
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        elif self.TokenSet[self.index][1] in arr :
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.index=last_index
            return False

    def array_list1(self):
        last_index = self.index
        List=[]
        res, obj = self.exp_array()
        if res:
            List.append(obj)
            res2, obj2 = self.array_list2()
            if res2:
                List.append(obj2)
                if self.TokenSet[self.index][1]=="]":  
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    return True, List
            self.index = last_index
            return False 
        else:
            return False

    def array_list2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Array_List2"].split("?")  
        List=[]
        if self.TokenSet[self.index][1]==",":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.exp_array()
            if res:
                List.append(obj)
                res2, obj2 = self.array_list2(),
                if res2:
                    List.append(obj2)
                    return True, List
            self.index = last_index
            return False
        elif self.TokenSet[self.index][1]=="]":  
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        elif self.TokenSet[self.index][1] in arr:  
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            self.index=last_index
            return False
    
    def exp_array(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["EXP_ARRAY"].split("?")
        List = []
        res, obj = self.OE()
        if res:
            List.append(obj)
            return True, List

        self.index= last_index
        res2, obj2 = self.A1()
        if res2:
            List.append(obj2)
            return True, List

        if self.TokenSet[self.index][1] in arr:  
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        else:
            return False, []




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

    def MST(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MST"].split("?")
        List=[]
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
            List.append(self.TokenSet[self.index])
            return True, List
        self.index=last_index
        res, obj = self.SST()
        if res:
            List.append(obj)
            self.MST()
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True , List
        self.index=last_index
        return False

    def switch(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1] == "switch":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1] == "(":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res, obj = self.OE()
                if res:
                    List.append(self.TokenSet[self.index])
                    if self.TokenSet[self.index][1] == ")":
                        List.append(self.TokenSet[self.index])
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            List.append(self.TokenSet[self.index])
                            self.index+=1
                            res2, obj2 = self.SwitchBody()
                            if res2:
                                List.append(obj2)
                                res3, obj3 = self.default()
                                if res3:
                                    List.append(obj3)
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        List.append(self.TokenSet[self.index])   
                                        self.index+=1
                                        return , List
                self.index=last_index
                return False
        else:
            self.index=last_index
            return False


    def SwitchBody(self):
        last_index=self.index
        List=[]
        if self.TokenSet[self.index][1] == "case":
            List.append(self.TokenSet[self.index])
            self.index+=1
            res, obj = self.Id_const()
            if res:
                List.append(obj)
                if self.TokenSet[self.index][1] == ":":
                    List.append(self.TokenSet[self.index])
                    self.index+=1
                    res2, obj2= self.MST()
                    if res2:
                        List.append(obj2)
                        res3, obj3 = self.SwitchBody()
                        if res3:
                            return True, List
            self.index = last_index
            return False, List
        else:
            self.index=last_index
            return False

    def default(self):
        last_index=self.index
        List= []
        if self.TokenSet[self.index][1] == "default":
            List.append(self.TokenSet[self.index])
            self.index+=1
            if self.TokenSet[self.index][1] == ":":
                List.append(self.TokenSet[self.index])
                self.index+=1
                res2, obj = self.MST()
                if res2:
                    List.append(self.TokenSet[self.index])
                    return True
            self.index=last_index
            return False
        self.index=last_index
        self.errors.append("Invalid Default Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def AM(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AM"].split("?")        
        List=[]
        if self.TokenSet[self.index][1] == "Class":
            return True , []
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])            
            self.index+=1
            return True, List
        self.index=last_index
        self.errors.append("Invalid Access Modifier Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def defs(self):
        # Opening JSON file
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Defs"].split("?")
        List=[]
        if self.TokenSet[self.index][1] == "@":
            return True , []       
        if self.TokenSet[self.index][1] == "Class":
            return True . []
        if self.TokenSet[self.index][1] in arr:
            List.append(self.TokenSet[self.index])
            self.index+=1
            return True, List
        self.errors.append("Invalid Defination at Line # {}".format(self.TokenSet[self.index][2]))
        self.index=last_index
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

# rulees : check krwaoo baad mai index mai +1 krwaoo , hr cfg ka fn object return krega
# hr cfg ka fn token ki list retrun krega and then we add this in our cdt
# sb say pehlay return ka dekhra hn ======== laga dunga fn k upr 
# phr cd mai add ka dekhunga hr cfg keliye

# cb , fn_dec, class kay fn dekhnay prayngay 

# cdt mai add krwatay wqt dekhunga k list return kr ra hai object ya sirf aik object hr function keliye 
# ju ju fn list return kr re hain wo jhn jhn call huray hain aik baar dekhlo
# jhn jhn fn cxall hue hain whn list mai say append krwana parayga 