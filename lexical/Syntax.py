import json
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

    # starting cfg k saray rules k function ki validation fn is function k andar likhu
    def s(self):
        if self.defs():
            if self.AM():
                if self.CM():
                    if self.TokenSet[self.index][0]=="Class":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1
                            if self.INH_IMP():
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                    self.index+=1
                                    if True:
                                        if self.TokenSet[self.index][1]=="void":
                                            self.index+=1
                                            if self.TokenSet[self.index][1]=="Java":
                                                self.index+=1
                                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                                                    self.index+=1
                                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                                                        self.index+=1
                                                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                                            self.index+=1
                                                            if self.MST():
                                                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                                    self.index+=1
                                                                    if self.cb():
                                                                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                                            print("Close")
                                                                            self.index+=1
                                                                            if self.defs():
                                                                                return True
        else:
            return False

    def defs(self):
        # Opening JSON file
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Defs"].split("?")
        if self.TokenSet[self.index][1] == "@":
            return True        
        elif self.TokenSet[self.index][1] == "Class":
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.errors.append("Invalid Defination at Line # {}".format(self.TokenSet[self.index][2]))
            self.index=last_index
            return False

    def MST(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MST"].split("?")
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
            return True
        elif self.SST():
            self.MST()
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True

        self.index=last_index
        return False

    def switch(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "switch":
            self.index+=1
            if self.TokenSet[self.index][1] == "(":
                self.index+=1
                if self.OE():
                    if self.TokenSet[self.index][1] == ")":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            self.index+=1
                            if self.SwitchBody():
                                if self.default():
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        else:
            self.index=last_index
            return False

    def SwitchBody(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "case":
            self.index+=1
            if self.Id_const():
                if self.TokenSet[self.index][1] == ":":
                    self.index+=1
                    if self.MST():
                        if self.SwitchBody():
                            return True
        else:
            self.index=last_index
            return False

    def default(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "default":
            self.index+=1
            if self.TokenSet[self.index][1] == ":":
                self.index+=1
                if self.MST():
                    return True

        self.index=last_index
        self.errors.append("Invalid Default Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def Class(self):
        last_index=self.index
        if self.AM():
            if self.CM():
                if self.TokenSet[self.index][0]=="Class":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Identifier":
                        self.index+=1
                        if self.INH_IMP():
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                self.index+=1
                                if self.cb():
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        self.index=last_index
        # self.errors.append("Invalid Class Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def AM(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AM"].split("?")        
        if self.TokenSet[self.index][1] == "Class":
            return True 
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            # self.errors.append("Invalid Access Modifier Statement at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def CM(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["CM"].split("?")       
        if self.TokenSet[self.index][1] == "Class":
            return True 
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            # self.errors.append("Invalid Class Modifier Statement at Line # {}".format(self.TokenSet[self.index][2]))
            # return False

    def INH_IMP(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INH_IMP"].split("?")       
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
            return True
        elif self.TokenSet[self.index][1]=="extends":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                return True
        elif self.TokenSet[self.index][1]=="Implements":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            self.errors.append("Invalid Inheritance or implementation Statement at Line # {}".format(self.TokenSet[self.index][2]))
            return False
    
    def attribute(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ATTRIBUTE"].split("?")      
        if self.Dec():
            return True
        elif self.assign_st():
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            self.errors.append("Invalid Attribute  at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def cb(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["CB"].split("?")    
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
            return True                                                  
        elif self.attribute():
            self.cb()
        elif self.Fn_def():
            self.cb()
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            # self.errors.append("Invalid Class Body at Line # {}".format(self.TokenSet[self.index][2]))
            return False
    
    def while_st(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="while":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.OE():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                self.index+=1
                                if self.body():
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        self.index=last_index
        # self.errors.append("Invalid While Statement Body at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def while_condition(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        if self.Id_const():
            if self.TokenSet[self.index][1] in arr:
                self.index+=1
                if self.Id_const():
                    return True
        else:
            self.index=last_index
            self.errors.append("Invalid While Condition at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def If_condition(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        if self.Id_const():
            if self.TokenSet[self.index][1] in arr:
                self.index+=1
                if self.Id_const():
                    return True
        else:
            self.index=last_index
            self.errors.append("Invalid If Condition at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def Id_const(self):
        last_index=self.index
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1        
            return True
        elif self.const():
            return True
        else:
            self.index=last_index
            self.errors.append("Invalid Identifier or constant at Line # {}".format(self.TokenSet[self.index][2]))
            return False
    
    def const(const):
        last_index=self.index
        Float_regex = '[+-]?[0-9]+\.[0-9]+'
        Int_regex='[+-]?[0-9]+'
        if(re.search(Float_regex,self.TokenSet[self.index][0])): 
            self.index+=1
            return True
        elif(re.search(Int_regex,self.TokenSet[self.index][0])): 
            self.index+=1
            return True
        else:
            self.index=last_index
            self.errors.append("Invalid Const at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def body(self):
        last_index=self.index
        if self.MST():
            return True
        self.index=last_index
        self.errors.append("Invalid  Body at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def function_call(self):
        last_index= self.index
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1        
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.param_list():    
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        self.index+=1 
                        if self.TokenSet[self.index][1]==";":
                            self.index+=1 
                            return True
        self.index=last_index
        # self.errors.append("Invalid Function Call at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def param_list(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARAM_LIST"].split("?")  
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            if self.para2():
                return True     
        elif self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
        else:
            self.index=last_index
            self.errors.append("Invalid Param List at Line # {}".format(self.TokenSet[self.index][2]))
            return False
    
    def para2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARA_LIST2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1 
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.para2():
                    return True
        elif self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
        else:
            self.index=last_index
            return False

    def for_st(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="range":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.k1():
                    if self.TokenSet[self.index][1]==";":
                        self.index+=1
                        if self.OE():
                            if self.TokenSet[self.index][1]==";":
                                self.index+=1
                                if self.k3():
                                    if self.TokenSet[self.index][1]==")":
                                        self.index+=1
                                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                            self.index+=1
                                            if self.body():
                                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                    self.index+=1
                                                    return True
        self.index=last_index
        # self.errors.append("Invalid For Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def k1():
        if self.Dec():
            return True
        elif self.assign_st():
            return True
        else:
            return False

    def k3():
        if self.inc_dec():
            if self.k():
                return True
        elif self.k():
            if self.inc_dec():
                return True
        else:
            return False

    def k():
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        elif self.function_call():
            return True
        elif self.obj():
            return True
        elif self.Array():
            return True
        else:
            return False

    def obj(self):
        last_index=self.index
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            if self.TokenSet[self.index][1]==".":
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    self.obj2()
        self.index=last_index
        return False
    
    def obj2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["OBJ2"].split("?")  
        if self.TokenSet[self.index][1]==".":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                self.obj2()
        elif self.TokenSet[self.index][1] in arr:
                self.index+=1
        else:
            return False

    def inc_dec(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INC_DEC"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
        else:
            self.index=last_index
            self.errors.append("Invalid Increment Or Decrement Operator at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def interface(self):
        last_index=self.index
        if self.TokenSet[self.index][0]=="Interface":
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                        self.index+=1
                        if self.MST():
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                self.index+=1
                                return True
        self.index=last_index
        # self.errors.append("Invalid Interface defination Operator at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def Dec(self):
        last_index=self.index
        if self.dt():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.INIT():
                    if self.List():
                        return True
        self.index=last_index
        # self.errors.append("Invalid Declaration Operator at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def dt(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.errors.append("Invalid Data Type at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def INIT(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        # print(self.TokenSet[self.index][1])
        if self.TokenSet[self.index][1]=="=":   
            self.index+=1
            if self.OE():
                return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
        else:
            self.index=last_index
            self.errors.append("Invalid Init at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def LIST(self):
        last_index=self.index
        if self.TokenSet[self.index][1]==";":   
            self.index+=1
            return True
        elif self.TokenSet[self.index][1]==",":   
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.INIT():
                    if self.List():
                        return True
        else:
            self=last_index
            self.errors.append("Invalid List Operator at Line # {}".format(self.TokenSet[self.index][2]))
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

    def Rt(self):
        if self.dt():
            return True
        elif self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        elif self.dt():
            if self.Rt1():
                return True
        elif self.TokenSet[self.index][1]=="void":
            self.index+=1
            return True
        else:
            return False

    def Rt1(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                self.index+=1
                if self.Rt2():
                    return True
        self.index=last_index
        return False
    
    def Rt2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        if self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                self.index+=1
                if self.Rt2():
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        self.index=last_index
        return False
    
    def Obj_dec(self):
        last_index=self.index
        if self.class_name():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.TokenSet[self.index][1]=="=":
                    self.index+=1
                    if self.TokenSet[self.index][1]=="new":
                        self.index+=1
                        if self.class_name():
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                                self.index+=1
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                                    self.index+=1
                                    if self.TokenSet[self.index][1]==";":
                                        return True
        self.index=last_index
        # self.errors.append("Invalid Object Declaration at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def class_name(self):
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        else:
            return False

    def parameter(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARAMETER"].split("?")  
        if self.dt():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.p1():
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            self.errors.append("Invalid Parametre at Line # {}".format(self.TokenSet[self.index][2]))
            return False
            
    def p1(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["P1"].split("?")  
        if self.TokenSet[self.index][1] == "=":
            self.index+=1
            if self.OE():
                if self.p2():
                    return True
        elif self.p2():
            return True
        elif self.TokenSet[self.index][1] in arr:
            return True
        else:
            self.index=last_index
            return False

    def p2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["P2"].split("?")  
        if self.TokenSet[self.index][1] == "=":
            self.index+=1
            if self.dt():
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    if self.p1():
                        return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False


    def TRY(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "try":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.MST():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        last_index=self.index
        # self.errors.append("Invalid Try Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def CATCH(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "catch":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.TokenSet[self.index][1]=="Exception":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Identifier":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                self.index+=1
                                if self.MST():
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        self.index=last_index
        # self.errors.append("Invalid Catch Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def FINALLY(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "finally":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.MST():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        self.index=last_index
        # self.errors.append("Invalid Finally Statemnet at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def BREAK(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "break":
            self.index+=1
            if self.TokenSet[self.index][1] == ";":
                self.index+=1
                return True
        self.index=last_index
        # self.errors.append("Invalid Break Statemnet at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def CONTINUE(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "Continue":
            self.index+=1
            if self.TokenSet[self.index][1] == ";":
                self.index+=1
                return True
        self.index=last_index
        # self.errors.append("Invalid Continue statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def THROW(self):
        last_index=self.index
        if self.TokenSet[self.index][1] == "throw":
            self.index+=1
            if self.TokenSet[self.index][1] == "new":
                self.index+=1
                if self.ERROR_TYPE():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="String":
                            self.index+=1    
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                                self.index+=1
                                return True
        self.index=last_index
        # self.errors.append("Invalid Throw Operator at Line # {}".format(self.TokenSet[self.index][2]))
        return False 
                        
    def Error_type(self):
        arr= ['ArithmeticException','ClassNotFoundException','ArrayIndexOutOfBoundsException','SecurityException']
        if self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
        else:
            self.errors.append("Invalid Error Type for Throw statement Operator at Line # {}".format(self.TokenSet[self.index][2]))
            return False
    
    def assign_st(self):
        last_index=self.index
        if self.this():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1            
                if self.x1():
                    if self.INIT():
                        if self.LIST():
                            return True
        self.index=last_index
        # self.errors.append("Invalid Assignment  at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def assign_opt(self):
        if self.TokenSet[self.index][1]=="=":
            self.index+=1    
            return True
        elif self.c_assign():
            return True
        else:
            self.errors.append("Invalid Assignmengt  Operatoration at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def c_assign(self):
        last_index=self.index
        arr= ["+", "-", "*", "/", "%"]
        if self.TokenSet[self.index][1] in arr:
            self.index+=1    
            if self.TokenSet[self.index][1]=="=":
                self.index+=1    
                return True
        self.index=last_index
        return False

    def x1(self):
        last_index=self.index
        if self.TokenSet[self.index][1]==".":
            self.index+=1    
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1    
                if self.x():
                    return True
        elif self.TokenSet[self.index][1]=="[":
            self.index+=1    
            if self.const():
                if self.TokenSet[self.index][1]=="]":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                return True
        elif self.TokenSet[self.index][1]=="(":
            self.index+=1    
            if self.parameter():
                if self.TokenSet[self.index][1]==")":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                return True
        else:
            self.index=last_index
            return False

    def x(self):
        last_index=self.index
        if self.TokenSet[self.index][1]==".":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1    
                if self.x():
                    return True
        elif self.assign_opt():
            if self.OE():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1]=="[":
            self.index+=1    
            if self.const():
                if self.TokenSet[self.index][1]=="]":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                return True
        elif self.TokenSet[self.index][1]=="(":
            self.index+=1    
            if self.parameter():
                if self.TokenSet[self.index][1]==")":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                return True
        elif self.inc_dec():
            return True
        else:
            self.index=last_index
            return False

    def this(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["this"].split("?")  
        if self.TokenSet[self.index][1]=="this":
            self.index+=1
            if self.TokenSet[self.index][1]==".":
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True    
        self.index=last_index
        # self.errors.append("Invalid This statement at Line # {}".format(self.TokenSet[self.index][2]))        
        return False

    def OE(self):
        if self.AE():
            if self.OE2():
                return True
        return False
     
    def OE2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["OE2"].split("?")  
        if self.TokenSet[self.index][1]=="|":
                self.index+=1
                if self.TokenSet[self.index][1]=="|":
                    self.index+=1
                    if self.AE():
                        if OE2():
                            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False
    
    def AE(self):
        if self.RE():
            if self.AE2():
                return True
        else:
            return False
    
    def AE2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AE2"].split("?")  
        if self.TokenSet[self.index][1]=="&":
                self.index+=1
                if self.TokenSet[self.index][1]=="&":
                    self.index+=1        
                    if self.RE():
                        if self.AE2():
                            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

    def RE(self):
        if self.E():
            if self.RE2():
                return True
        return False

    def RE2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        arr1=data["RE2"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1                 
            if self.E():     
                if self.RE2():
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1                 
            return True
        else:
            return False


    def E(self):
        if self.T():
            if self.E2():    
                return True
        else:
            return False
    
    def E2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PM"].split("?")
        arr1=data["E2"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1  
            if self.T():
                if self.E2(): 
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

    def T(self):
        if self.F():     
            if self.T2(): 
                return True
        else:
            return False
    
    def T2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MDM"].split("?")
        arr1=data["T2"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1  
            if self.F():
                if self.T2():
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

    def F(self):
        last_index=self.index
        if self.this():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.F2(): 
                    return True
        elif self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            self.index+=1
            if self.OE():
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    return True
        elif self.TokenSet[self.index][1]=="!":
            if self.F():
                return True  
        elif self.inc_dec():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                return True
        else:
            self.index=last_index
            return False   
    
    def F2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["F2"].split("?") 
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            self.index+=1
            if self.PL():
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    self.index+=1
                    return True
        elif self.inc_dec():
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            self.index=last_index
            return False
    
    def PL(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL"].split("?")  
        if self.OE():
            if self.PL2():
                return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
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

    def SST(self):
        if self.Obj_dec():
            return True
        elif self.Fn_def():
            self.errors.pop()            
            return True
        elif self.Array():
            self.errors.pop()
            return True
        elif self.switch():
            self.errors.pop()
            return True
        elif self.Class():
            self.errors.pop()
            return True
        elif self.interface():
            self.errors.pop()
            return True
        elif self.while_st():
            self.errors.pop()
            return True
        elif self.function_call():
            self.errors.pop()
            return True
        elif self.for_st():
            self.errors.pop()
            return True
        elif self.If_Else():
            self.errors.pop()
            return True
        elif self.Dec():
            self.errors.pop()
            return True
        elif self.assign_st():
            self.errors.pop()
            return True
        elif self.TRY():
            self.errors.pop()
            return True
        elif self.CATCH():
            self.errors.pop()
            return True
        elif self.FINALLY():
            self.errors.pop()
            return True
        elif self.BREAK():
            self.errors.pop()
            return True
        elif self.THROW():
            self.errors.pop()
            return True
        elif self.CONTINUE():
            self.errors.pop()
            return True
        elif self.Return():
            self.errors.pop()
            return True
        else:
            self.errors.append("Invalid statment at Line # {}".format(self.TokenSet[self.index][2]))
            return False

    def Return(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="return":
            self.index+=1
            if self.case():
                if self.TokenSet[self.index][1]==";":
                    self.index+=1
                    return True
        self.index=last_index
        # self.errors.append("Invalid Return Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def case(self):
        if self.OE():
            return True       
        elif self.TokenSet[self.index][1]=="return":     
            self.index+=1
            return True       
        return False

    def If_Else(self):
        last_index=self.index
        if self.TokenSet[self.index][1]=="if":
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.OE():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            self.index+=1
                            if self.body():
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                    self.index+=1
                                    if self.Else():
                                        return True 
        self.index=last_index   
        # self.errors.append("Invalid If / Else  at Line # {}".format(self.TokenSet[self.index][2]))        
        return False

    
    def Else(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Else"].split("?")  
        if self.TokenSet[self.index][1]=="else":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.body():
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True      
        self.index=last_index      
        self.errors.append("Invalid Else Statement at Line # {}".format(self.TokenSet[self.index][2]))
        return False

    def Array(self):
        last_index=self.index
        if self.dt():
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.A():
                    if self.B():
                        if self.A1():
                            if self.TokenSet[self.index][1]==";":
                                return 
        self.index=last_index
        # self.errors.append("Invalid Array at Line # {}".format(self.TokenSet[self.index][2]))
        return False
    
    def A(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A"].split("?")  
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            self.index+=1
            return True
        elif self.A3():
            self.index+=1
        else:
            self.index=last_index
            return False
    
    def A3(self):
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="]":       
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="]":       
                        self.index+=1 
                        return True
        return False

    def A1(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A1"].split("?")  
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.array_list1():
                return True
        elif self.TokenSet[self.index][1] in arr :
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

    def B(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["B"].split("?")  
        if self.TokenSet[self.index][1]=="=":  
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr :
            self.index+=1
            return True
        else:
            self.index=last_index
            return False

    def array_list1(self):
        if self.exp_array():
            if self.array_list2():
                if self.TokenSet[self.index][1]=="]":  
                    self.index+=1
                    return True
        else:
            return False

    def array_list2(self):
        last_index=self.index
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Array_List2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1
            if self.exp_array():
                if self.array_list2():
                    return True
        elif self.TokenSet[self.index][1]=="]":  
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr:  
            self.index+=1
            return True
        else:
            self.index=last_index
            return False
    
    def exp_array(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["EXP_ARRAY"].split("?")
        if self.OE():
            return True
        elif self.A1():
            return True
        elif self.TokenSet[self.index][1] in arr:  
            self.index+=1
            return True
        else:
            return False
    


# we have to remove multi line comments and  error 
import re
# staring is incomplete
# switchBody is incomplete
# boolean add huga 
# agr close find huga tu skay end mai hamsha endmarker check huga 

a = open(r'token.txt','r')
x=a.read().split("?")
arr=[]

for i in x:
    string_without_brackets = i.strip("()")
    arr.append(string_without_brackets.split(","))
# print(arr)

obj = SA(arr)
print("Token Validation : " ,obj.validate(),"  ,Current Token IS : ", obj.TokenSet[obj.index], ",  Index IS : ", obj.index)

for errors in obj.errors:
    print(errors )

