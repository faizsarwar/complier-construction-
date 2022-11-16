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

