import json
class SA:
    def __init__(self, TokenSet):
        self.TokenSet = TokenSet
        self.index = 0


    def validate(self):
        if self.s():
            if (self.TokenSet[self.index]=="@"):
                return True
        return False

    # starting cfg k saray rules k function ki validation fn is function k andar likhu
    def s(self):
        if self.defs():
            print("def")
            if self.AM():
                print("Am")
                if self.CM():
                    print("CM")
                    if self.TokenSet[self.index][0]=="Class":
                        print("Class")
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1
                            if True:
                                # self.index+=1
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                    print("open")
                                    self.index+=1
                                    #ye cond rem kro
                                    if True:
                                        # self.index+=1
                                        if self.TokenSet[self.index][1]=="void":
                                            print("void")
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
                                                                self.index+=1
                                                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                                    self.index+=1
                                                                    if self.cb():
                                                                        self.index+=1
                                                                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                                            self.index+=1
                                                                            if self.defs():
                                                                                self.index+=1
                                                                                return True
        else:
            return False

    def defs(self):
        # Opening JSON file
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Defs"].split("?")
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return True

    def MST(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MST"].split("?")
        if self.SST():
            self.index+=1
            self.MST()
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        return False

    def switch(self):
        if self.TokenSet[self.index][1] == "switch":
            self.index+=1
            if self.TokenSet[self.index][1] == "(":
                self.index+=1
                if self.OE():
                    self.index+=1
                    if self.TokenSet[self.index][1] == ")":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            self.index+=1
                            if self.SwitchBody():
                                self.index+=1
                                if self.default():
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        else:
            return False


    def SwitchBody(self):
        if self.TokenSet[self.index][1] == "case":
            self.index+=1
            if self.Id_const():
                self.index+=1
                if self.TokenSet[self.index][1] == ":":
                    self.index+=1
                    if self.MST():
                        self.index+=1
                        if self.SwitchBody():
                            return True
        else:
            return False

    def default(self):
        if self.TokenSet[self.index][1] == "default":
            self.index+=1
            if self.TokenSet[self.index][1] == ":":
                self.index+=1
                if self.MST():
                    self.index+=1
                    return True
        return False

    def Class(self):
        if self.AM():
            self.index+=1
            if self.CM():
                self.index+=1
                if self.TokenSet[self.index][0]=="Class":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Identifier":
                        self.index+=1
                        if self.inh_imp():
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                self.index+=1
                                if self.cb():
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        return False

    def AM(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AM"].split("?")        
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return True

    def CM(self):
            f = open('SolutionSets.json')
            data = json.load(f)
            arr=data["CM"].split("?")        
            if self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
            else:
                return True

    def inh_imp(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INH_IMP"].split("?")       
        if self.TokenSet[self.index][1]=="extends":
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
            return False

    
    
    def attribute(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ATTRIBUTE"].split("?")      
        if self.declaration():
            self.index+=1
            return True
        elif self.assignment():
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False

    def cb(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["CB"].split("?")      
        if self.attribute():
            self.index+=1
            self.cb()
        elif self.Fn_def():
            self.index+=1
            self.cb()
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False
    
    def while_st(self):
        if self.TokenSet[self.index][1]=="while":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.while_condition():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                self.index+=1
                                if self.body():
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        return False
    
    def while_condition(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        if self.Id_const():
            self.index+=1
            if self.TokenSet[self.index][1] in arr:
                self.index+=1
                if self.Id_const():
                    self.index+=1
                    return True
        else:
            return False

    def If_condition(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["ROP"].split("?")  
        if self.Id_const():
            self.index+=1
            if self.TokenSet[self.index][1] in arr:
                self.index+=1
                if self.Id_const():
                    self.index+=1
                    return True
        else:
            return False

    def Id_const(self):
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1        
            return True
        elif self.const():
            self.index+=1
            return True
        else:
            return False
    
    def const(const):
        Float_regex = '[+-]?[0-9]+\.[0-9]+'
        Int_regex='[+-]?[0-9]+'
        if(re.search(Float_regex,self.TokenSet[self.index][0])): 
            self.index+=1
            return True
        elif(re.search(Int_regex,self.TokenSet[self.index][0])): 
            self.index+=1
            return True
        else:
            return False

    def body():
        if self.MST():
            self.index+=1
            return True
        return False
    
    def function_call():
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1        
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.param_list():
                    self.index+=1        
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        self.index+=1 
                        if self.TokenSet[self.index][1]==";":
                            self.index+=1 
                            return True
        return False

    def param_list(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARAM_LIST"].split("?")  
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            if self.param_list2():
                self.index+=1 
                return True     
        elif self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
        else:
            return False
    
    def param_list2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARA_LIST2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1 
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.param_list2():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
                self.index+=1
                return True
        else:
            return False

    def for_st(self):
        if self.TokenSet[self.index][1]=="range":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.k1():
                    self.index+=1
                    if self.TokenSet[self.index][1]==";":
                        self.index+=1
                        if self.OE():
                            self.index+=1
                            if self.TokenSet[self.index][1]==";":
                                self.index+=1
                                if self.k3():
                                    self.index+=1
                                    if self.TokenSet[self.index][1]==")":
                                        self.index+=1
                                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                            self.index+=1
                                            if self.body():
                                                self.index+=1
                                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                    self.index+=1
                                                    return True
        return False
    
    def k1():
        if self.declaration():
            self.index+=1
            return True
        elif self.assignment():
            self.index+=1
            return True
        else:
            return False

    def k3():
        if self.incr_dec():
            self.index+=1
            if self.k():
                self.index+=1
                return True
        elif self.k():
                self.index+=1
                if self.incr_deck():
                    self.index+=1
                    return True
        else:
            return False

    def k():
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        elif self.function_call():
            self.index+=1
            return True
        elif self.obj():
            self.index+=1
            return True
        elif self.Array():
            self.index+=1
            return True
        else:
            return False

    def obj(self):
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            if self.TokenSet[self.index][1]==".":
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    self.obj2()
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

    def incr_dec(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["INC_DEC"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
        else:
            return False

    def interface_def(self):
        if self.TokenSet[self.index][0]=="Interface":
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                        self.index+=1
                        if self.MST():
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                self.index+=1
                                return True
        return False

    def declaration(self):
        if self.dt():
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.Init():
                    self.index+=1
                    if self.List():
                        self.index+=1
                        return True
        return False

    def dt(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1
        else:
            return False

    def Init(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        if self.TokenSet[self.index][1]=="=":   
            self.index+=1
            if self.OE():     
                self.index+=1
                return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
        else:
            return False

    def List(self):
        if self.TokenSet[self.index][1]==";":   
            self.index+=1
            return True
        elif self.TokenSet[self.index][1]==",":   
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.Init():
                    self.index+=1
                    if self.List():
                        self.index+=1
                        return True
        else:
            return False

    def Fn_def(self):
        if self.TokenSet[self.index][1]=="def":   
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                    self.index+=1
                    if self.parameter():
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                            self.index+=1
                            if self.TokenSet[self.index][1]==":":   
                                self.index+=1
                                if self.Rt():
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                                        self.index+=1
                                        if self.MST():
                                            self.index+=1
                                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                                self.index+=1
                                                return True
        return False

    def Rt(self):
        if self.dt():
            self.index+=1
            return True
        elif self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        elif self.dt():
            self.index+=1
            if self.Rt1():
                self.index+=1
                return True
        elif self.TokenSet[self.index][1]=="void":
            self.index+=1
            return True
        else:
            return False

    def Rt1(self):
        if self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                self.index+=1
                if self.Rt2():
                    self.index+=1
                    return True
        return False
    
    def Rt2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["dt"].split("?")  
        if self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][1]=="]":
                self.index+=1
                if self.Rt2():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        return False
    
    def Obj_dec(self):
        if self.class_name():
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.TokenSet[self.index][1]=="=":
                    self.index+=1
                    if self.TokenSet[self.index][1]=="new":
                        self.index+=1
                        if self.class_name():
                            self.index+=1
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                                self.index+=1
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                                    self.index+=1
                                    if self.TokenSet[self.index][1]==";":
                                        return True
        return False

    def class_name(self):
        if self.TokenSet[self.index][0]=="Identifier":
            self.index+=1
            return True
        else:
            return False

    def parameter(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PARAMETER"].split("?")  
        if self.dt():
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.p1():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False
    def p1(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["P1"].split("?")  
        if self.TokenSet[self.index][1] == "=":
            self.index+=1
            if self.OE():
                self.index+=1
                if self.p2():
                    self.index+=1
                    return True
        elif self.p2():
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False

    def p2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["P2"].split("?")  
        if self.TokenSet[self.index][1] == "=":
            self.index+=1
            if self.dt():
                self.index+=1
                if self.TokenSet[self.index][0]=="Identifier":
                    self.index+=1
                    if self.p1():
                        self.index+=1
                        return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False


    def TRY(self):
        if self.TokenSet[self.index][1] == "try":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.MST():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        return False

    def Catch(self):
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
                                    self.index+=1
                                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                        self.index+=1
                                        return True
        return False

    def Finally(self):
        if self.TokenSet[self.index][1] == "finally":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.MST():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        return False

    def BREAK(self):
        if self.TokenSet[self.index][1] == "break":
            self.index+=1
            if self.TokenSet[self.index][1] == ";":
                self.index+=1
                return True
        return False

    def Continue(self):
        if self.TokenSet[self.index][1] == "Continue":
            self.index+=1
            if self.TokenSet[self.index][1] == ";":
                self.index+=1
                return True
        return False

    def throw(self):
        if self.TokenSet[self.index][1] == "throw":
            self.index+=1
            if self.TokenSet[self.index][1] == "new":
                self.index+=1
                if self.Error_type():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="String":
                            self.index+=1    
                            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                                self.index+=1
                   
    def Error_type(self):
        arr= ['ArithmeticException','ClassNotFoundException','ArrayIndexOutOfBoundsException','SecurityException']
        if self.TokenSet[self.index][1] in arr :
                self.index+=1
                return True
        else:
            return False
    
    def assignment(self):
        if self.this():
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1            
                if self.x1():
                    self.index+=1
                    if self.Init():
                        self.index+=1
                        if self.List():
                            self.index+=1
                            return True
        return False
    
    def Assign_op(self):
        if self.TokenSet[self.index][1]=="=":
            self.index+=1    
            return True
        elif self.c_Assign():
            self.index+=1  
            return True
        else:
            return False

    def c_Assign(self):
        arr= ["+", "-", "*", "/", "%"]
        if self.TokenSet[self.index][1] in arr:
            self.index+=1    
            if self.TokenSet[self.index][1]=="=":
                self.index+=1    
                return True
        return False

    def x1(self):
        if self.TokenSet[self.index][1]==".":
            self.index+=1    
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1    
                if self.x():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1]=="[":
            self.index+=1    
            if self.const():
                self.index+=1
                if self.TokenSet[self.index][1]=="]":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                self.index+=1
                                return True
        elif self.TokenSet[self.index][1]=="(":
            self.index+=1    
            if self.parameter():
                self.index+=1
                if self.TokenSet[self.index][1]==")":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                self.index+=1
                                return True
        else:
            return False

    def x(self):
        if self.TokenSet[self.index][1]==".":
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1    
                if self.x():
                    self.index+=1
                    return True
        elif self.Assign_op():
            self.index+=1
            if self.OE():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1]=="[":
            self.index+=1    
            if self.const():
                self.index+=1
                if self.TokenSet[self.index][1]=="]":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                self.index+=1
                                return True
        elif self.TokenSet[self.index][1]=="(":
            self.index+=1    
            if self.parameter():
                self.index+=1
                if self.TokenSet[self.index][1]==")":
                    self.index+=1
                    if self.TokenSet[self.index][1]==".":
                        self.index+=1    
                        if self.TokenSet[self.index][0]=="Identifier":
                            self.index+=1    
                            if self.x():
                                self.index+=1
                                return True
        elif self.incr_dec():
            self.index+=1
            return True
        else:
            return False

    def this(self):
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
        return False

    def OE(self):
        if self.AE():
            self.index+=1
            if self.OE2():
                self.index+=1
                return True
        return False
     
    def OE2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["OE2"].split("?")  
        if self.TokenSet[self.index][1]=="|":
                self.index+=1
                if self.TokenSet[self.index][1]=="|":
                    self.index+=1
                    if self.AE():
                        self.index+=1
                        if OE2():
                            self.index+=1
                            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False
    
    def AE(self):
        if self.RE():
            self.index+=1
            if self.AE2():
                self.index+=1
                return True
        else:
            return False
    
    def AE2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["AE2"].split("?")  
        if self.TokenSet[self.index][1]=="&":
                self.index+=1
                if self.TokenSet[self.index][1]=="&":
                    self.index+=1        
                    if self.RE():
                        self.index+=1
                        if self.AE2():
                            self.index+=1
                            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False

    def RE(self):
        if self.E():
            self.index+=1        
            if self.RE2():
                self.index+=1
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
                self.index+=1        
                if self.RE2():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1                 
            return True
        else:
            return False


    def E(self):
        if self.T():
            self.index+=1     
            if self.E2():
                self.index+=1     
                return True
        else:
            return False
    
    def E2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PM"].split("?")
        arr1=data["E2"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1  
            if self.T():
                self.index+=1  
                if self.E2():
                    self.index+=1  
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1
            return True
        else:
            return False

    def T(self):
        if self.F():
            self.index+=1     
            if self.T2():
                self.index+=1     
                return True
        else:
            return False
    #
    def T2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["MDM"].split("?")
        arr1=data["T2"].split("?")  
        if self.TokenSet[self.index][1] in arr:
            self.index+=1  
            if self.F():
                self.index+=1  
                if self.T2():
                    self.index+=1  
                    return True
        elif self.TokenSet[self.index][1] in arr1:
            self.index+=1
            return True
        else:
            return False

    def F():
        if self.this():
            self.index+=1  
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.F2():
                    self.index+=1  
                    return True
        elif self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            self.index+=1
            if self.OE():
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1]=="!":
            if self.F():
                self.index+=1
                return True  
        elif self.incr_dec():    
            self.index+=1  
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                return True
        else:
            return False   
    
    def F2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["F2"].split("?") 
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
            self.index+=1
            if self.PL():
                self.index+=1
                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                    self.index+=1
                    return True
        elif self.incr_dec():
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False
    
    def PL(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL"].split("?")  
        if self.OE():
            self.index+=1
            if self.PL2():
                self.index+=1
                return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False

    def PL2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["PL2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1
            if self.OE():
                self.index+=1
                if self.PL2():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False

    def SST(self):
        if self.Obj_dec():
            self.index+=1
            return True
        elif self.Fn_def():
            self.index+=1
            return True
        elif self.Array():
            self.index+=1
            return True
        elif self.switch():
            self.index+=1
            return True
        elif self.Fn_def():
            self.index+=1
            return True
        elif self.Class():
            self.index+=1
            return True
        elif self.interface_def():
            self.index+=1
            return True
        elif self.while_st():
            self.index+=1
            return True
        elif self.function_call():
            self.index+=1
            return True
        elif self.for_st():
            self.index+=1
            return True
        elif self.If_Else():
            self.index+=1
            return True
        elif self.declaration():
            self.index+=1
            return True
        elif self.assignment():
            self.index+=1
            return True
        elif self.TRY():
            self.index+=1
            return True
        elif self.Catch():
            self.index+=1
            return True
        elif self.Finally():
            self.index+=1
            return True
        elif self.BREAK():
            self.index+=1
            return True
        elif self.throw():
            self.index+=1
            return True
        elif self.Continue():
            self.index+=1
            return True
        elif self.Return():
            self.index+=1
            return True
        else:
            return False

    def Return(self):
        if self.TokenSet[self.index][1]=="return":
            self.index+=1
            if self.case():
                self.index+=1
                if self.TokenSet[self.index][1]==";":
                    self.index+=1
                    return True
        return False
    
    def case(self):
        if self.OE():
            self.index+=1
            return True       
        elif self.TokenSet[self.index][1]=="return":     
            self.index+=1
            return True       
        return False

    def If_Else(self):
        if self.TokenSet[self.index][1]=="if":
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="(":
                self.index+=1
                if self.OE():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]==")":
                        self.index+=1
                        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                            self.index+=1
                            if self.body():
                                self.index+=1
                                if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                                    self.index+=1
                                    if self.Else():
                                        self.index+=1
                                        return True            
        return False

    
    def Else(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Else"].split("?")  
        if self.TokenSet[self.index][1]=="else":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="open":
                self.index+=1
                if self.body():
                    self.index+=1
                    if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="close":
                        self.index+=1
                        return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True            
        return False

    def Array(self):
        if self.dt():
            self.index+=1
            if self.TokenSet[self.index][0]=="Identifier":
                self.index+=1
                if self.A():
                    self.index+=1
                    if self.B():
                        self.index+=1
                        if self.A1():
                            self.index+=1
                            if self.TokenSet[self.index][1]==";":
                                return True
        return False
    
    #
    def A(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A"].split("?")  
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="]":
                self.index+=1
                if self.A():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1] in arr:
            self.index+=1
            return True
        else:
            return False
    #
    def A1(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["A1"].split("?")  
        if self.TokenSet[self.index][0]=="Bracket" and self.TokenSet[self.index][1]=="[":
            self.index+=1
            if self.array_list1():
                self.index+=1
                return True
        elif self.TokenSet[self.index][1] in arr :
            self.index+=1
            return True
        else:
            return False
    #
    def B(self):
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
            return False

    def array_list1(self):
        if self.exp_array():
            self.index+=1
            if self.array_list2():
                self.index+=1
                if self.TokenSet[self.index][1]=="]":  
                    self.index+=1
                    return True
        else:
            return False

    #
    def array_list2(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["Array_List2"].split("?")  
        if self.TokenSet[self.index][1]==",":
            self.index+=1
            if self.exp_array():
                self.index+=1
                if self.array_list2():
                    self.index+=1
                    return True
        elif self.TokenSet[self.index][1]=="]":  
            self.index+=1
            return True
        elif self.TokenSet[self.index][1] in arr:  
            self.index+=1
            return True
        else:
            return False
    
    def exp_array(self):
        f = open('SolutionSets.json')
        data = json.load(f)
        arr=data["EXP_ARRAY"].split("?")
        if self.OE():
            self.index+=1
            return True
        elif self.A1():
            self.index+=1
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
# boolean add huga bc

a = open(r'token.txt','r')
x=a.read().split("?")
arr=[]

for i in x:
    string_without_brackets = i.strip("()")
    arr.append(string_without_brackets.split(","))
# print(arr)

obj = SA(arr)
print(obj.validate(), obj.TokenSet[obj.index])