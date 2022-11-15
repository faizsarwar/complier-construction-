import re
import string
# class

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
Plus_Minus = '+-'
Mul_Div_Mod = '*/%'
Compound = ['+=', '*=', '-=', '/=', '%=']
Relational_Operation = ['<', '>', '<=', '>=', '!=', '==']
And_Logical = ['&&']
OR_Logical = ['||']
Brackets = ['(', ')', 'open', 'close', '[', ']']
Key_words = ["=",'boolean','this',"Java", 'char', 'int', 'double', 'Private', 'Protected', 'Final', 'try', 'catch', 'finally', 'throw', 'break', 'case', 'continue', 'while', 'range', 'switch',
             'if', 'else', 'extends','string', 'implements', 'new', 'return', 'Interface', 'this', 'throws', 'void', 'super', 'accept', 'decline', "null", 'def','const','main']
punctuators =[',',':',';','.']
class_ = ["Class", "class"]
id = r'^[A-Za-z_]+[A-Za-z0-9_]*'


# Error reporting
class Error:
    def __init__(self, position_start, position_end, error_name, details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.details = details

    # return error as string

    def asString(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.position_start.file_name}, line {self.position_start.line + 1}'
        f = open(
            r'./token.txt', 'a')
        f.write(
            f'({self.error_name},{self.details},{self.position_start.line})')
        return result

    # for not allowed characters


class IllegalCharError(Error):
    def __init__(self, position_start, position_end, details):
        super().__init__(position_start, position_end, 'Illegal Character', details)

class Position:
    def __init__(self, index, line, column, file_name, file_txt):
        self.index= index
        self.line= line
        self.column= column
        self.file_name= file_name
        self.file_txt = file_txt
    #creating method
    def next_pos(self, current_char):
        self.index += 1
        self.column +=1

        if current_char == '\n':
            self.line +=1
            self.column = 0
        
        return self

    def duplicate(self):
        return Position(self.index,self.line,self.column,self.file_name,self.file_txt)

#creating token 
class Token:
    def __init__(self, class_part, value = None, line_no = None):
        self.class_part = class_part
        self.value = value
        self.line_no = line_no

    def __repr__(self): #use to return obj in string representation 
        if self.value:
            return f'{self.class_part}:{self.value}:line{self.line_no}'
        return f'{self.class_part}:line{self.line_no}'

class lexeical:
    def __init__(self, file_name, txt):
        self.file_name=file_name
        self.txt= txt
        self.position = Position(-1 ,0, -1, file_name, txt)
        self.current_char = None
        self.next_pos()

    # def next_pos(self):
    #     self.position.next_pos(self.current_char)
    #     print(self.position.index,len(self.txt))
    #     if self.txt == None:
    #         return
    #     else:
    #         if self.position.index < len(self.txt):
    #             self.current_char = self.txt[self.position.index]
    #             print("change")
    #         else:
    #             self.txt = None
    #             self.current_char = None
    
    def next_pos(self):
        self.position.next_pos(self.current_char)
        self.current_char = self.txt[self.position.index] if self.position.index < len(
            self.txt) else None
    #token generate and save it into file
    def createTokens(self):
        token=[]
        while(self.current_char != None):
            position_start = self.position.duplicate()
            if self.current_char in ' \t':
                self.next_pos()
            if self.current_char in ' \n':
                self.next_pos()  
                # isClass
            # elif self.current_char in class_ :
            #     token.append(self.isClass())
            #     self.next_pos()
            elif self.current_char in Brackets:
                token.append(self.isBracket())
                self.next_pos()
            elif self.current_char == "=":
                token.append(self.isEqualsTo())
                self.next_pos()                
            elif self.current_char in punctuators:
                token.append(self.isPantuator())
                self.next_pos()
            elif self.current_char == "'":
                token.append(self.isChar())   
            elif self.current_char == '"':
                token.append(self.isString())
            elif self.current_char in re.findall('\d',self.current_char):
                token.append(self.isDigit())
            elif self.current_char in Compound:
                token.append(self.isCompound())
                self.next_pos()    
            elif self.current_char in Plus_Minus:
                token.append(self.isPlusMinus())
                self.next_pos()
            elif self.current_char in Mul_Div_Mod:
                token.append(self.isMDM())
                self.next_pos()
            elif self.current_char in Relational_Operation:
                token.append(self.isRO())
                self.next_pos()
            elif self.current_char == '#':  # checking whether comment is single line or multi line comment
                token.append(self.commentChecker())
            elif self.current_char in re.findall(id, self.current_char):
                token.append(self.isIdentifier())
            else:
                self.next_pos()
                return token , IllegalCharError(position_start, self.position, "'" + self.current_char + "'")
        return token,None 
                
    def isIdentifier(self):
        a = open(
            r'./token.txt','a'
        )
        id_str = ""
        position_start = self.position.duplicate()

        while self.current_char != None and self.current_char in re.findall(id,self.current_char):
            id_str += self.current_char
            self.next_pos()

        if id_str in Key_words:
            token_type = 'Keyword'
        elif id_str in Brackets:
            token_type = 'Bracket'
            a.write(f'({token_type},{id_str},{self.position.line+1})?')
            return Token(token_type,id_str,self.position.line+1)
        elif id_str in class_:
            token_type = 'Class'
            a.write(f'({token_type},Class,{self.position.line+1})?')
            return Token(token_type,id_str,self.position.line+1)
        else:
            token_type = 'Identifier'
        a.write(f'({token_type},{id_str},{self.position.line+1})?')
        return Token(token_type,id_str,self.position.line+1)
    
    def isString(self):
        f = open(
            r'./token.txt','a'
        )
        string = ''
        position_start = self.position.duplicate()
        escape_char=False
        
        self.next_pos()

        escape_chars = {
            'n' : '\n',
            't' : '\t'
        }
        while self.current_char != None and (self.current_char != '"'):
            if escape_char:
                string = string + escape_chars.get(self.current_char)
            else:
                string += self.current_char
            
            self.next_pos()


        if self.current_char=='"':
            f.write(f'(String,{string},{self.position.line+1})?')
            self.next_pos()
            return Token('String', string, self.position.line+1)
        else:
            a= IllegalCharError(position_start=position_start, position_end=self.position, details=string)
            print(a.asString())



    def isChar(self):
        # writing tokens
        f = open(
            r'./token.txt','a'
        )
        char = ''
        position_start = self.position.duplicate()
        escape_character = False
        self.next_pos()

        escape_characters = {
            'n': '\n',
            't': '\t'
        }
        while self.current_char != None and (self.current_char != "'" or escape_character):
            if escape_character:
                char += escape_characters.get(self.current_char,
                                              self.current_char)
            else:
                if self.current_char == '\\':
                    escape_character = True
                else:
                    char += self.current_char
                self.next_pos()
                escape_character = False
        if len(char) == 1 and self.current_char=="'":
            f.write(f'(Char,{char},{self.position.line+1})?')
            self.next_pos()
            return Token('Char', char, self.position.line+1)
        else:
            a= IllegalCharError(position_start=position_start, position_end=self.position, details=string)
            print(a.asString())

    def commentChecker(self):   #method checking whether comment is single line or multi line comment
        
        self.next_pos()

        if self.current_char != '$':
            #single line comment method
            f = open(
                r'./token.txt','a'
            )
            singleCommentStr = ''
            position_start = self.position.duplicate()
            
            while self.current_char != None and self.current_char != "\n":

                singleCommentStr += self.current_char
                self.next_pos()
                        
            self.next_pos()
            
            f.write(f'(Single line comment,{singleCommentStr},{self.position.line+1})?')
            return Token('Single line comment', singleCommentStr, self.position.line+1)

        else:
            #multi line comment method
            f = open(
                r'./token.txt','a'
            )
            multiCommentStr = ''
            position_start = self.position.duplicate()
            
            self.next_pos()

            while self.current_char != None:
                if self.current_char == "$":
                    self.next_pos()
                    if self.current_char == "#": #  #$ $#
                        break

                    else:
                        multiCommentStr = multiCommentStr + '$' + self.current_char
                        self.next_pos()
                        continue

                else:
                    multiCommentStr += self.current_char
                    self.next_pos()
                        
            self.next_pos()
            f.write(f'(Multi line comment,{multiCommentStr},{self.position.line+1})?')
            return Token('Multi line comment', multiCommentStr, self.position.line+1)
    def isDigit(self):

        # writing tokens
        f = open(
            r'./token.txt','a')
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.next_pos()

        if dot_count == 0:

            f.write(f'(int,{int(num_str)},{self.position.line+1})?')
            return Token('int', int(num_str), self.position.line+1)
        else:
            f.write(f'(double,{float(num_str)},{self.position.line+1})?')
            return Token('double', float(num_str), self.position.line+1)
    
    
    
    def isPlusMinus(self):
        # writing tokens
        f = open(
            r'./token.txt','a')
        compound_string = ''
        position_start = self.position.duplicate()
        token_type = ''
        while self.current_char != None and self.current_char in Plus_Minus:
            if self.current_char == '+':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                if compound_string in Compound:
                   token_type = 'Compound' 
                else:
                    token_type = 'PM'
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            else:
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                if compound_string in Compound:
                   token_type = 'Compound' 
                else:
                    token_type = 'PM'
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)

    def isMDM(self):
        # writing tokens
        compound_string = ''
        position_start = self.position.duplicate()
        token_type = ''
        f = open(
            r'./token.txt','a')
        while self.current_char != None and self.current_char in Mul_Div_Mod:
            if self.current_char == '*':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                token_type = 'Compound' if compound_string in Compound else 'MDM'
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            elif self.current_char == '/':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                token_type = 'Compound' if compound_string in Compound else 'MDM'
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            else:
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                token_type = 'Compound' if compound_string in Compound else 'MDM'
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)



    def isRO(self):
        # writing tokens
        compound_string = ''
        position_start = self.position.duplicate()
        token_type = 'RO'
        f = open(
            r'./token.txt','a')
        while self.current_char != None and self.current_char in Relational_Operation:
            if self.current_char == '<':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            elif self.current_char == '>':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            elif self.current_char == '!':
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
            else:
                compound_string += self.current_char
                self.next_pos()
                if self.current_char == '=':
                    compound_string += self.current_char
                f.write(f'({token_type},{compound_string},{self.position.line+1})?')
                return Token(token_type, compound_string, self.position.line+1)
    def isClass(self):
        # writing tokens
        f = open(
             r'./token.txt','a')
        while self.current_char != None and self.current_char in class_:
            f.write(f'(Class, Class,{self.position.line+1},)')
            return Token('Class', self.current_char, self.position.line+1)

    def isBracket(self):
        # writing tokens
        f = open(
             r'./token.txt','a')
        while self.current_char != None and self.current_char in Brackets:
            f.write(f'(Bracket,{self.current_char},{self.position.line+1})?')
            return Token('Bracket', self.current_char, self.position.line+1)

    def isEqualsTo(self):
        # writing tokens
        f = open(
             r'./token.txt','a')
        while self.current_char != None and self.current_char == '=':
            f.write(f'(Equals,{self.current_char},{self.position.line+1})?')
            return Token('Equals', self.current_char, self.position.line+1)
    def isPantuator(self):
        # writing tokens
        f = open(
             r'./token.txt','a')
        while self.current_char != None and self.current_char in punctuators:
            f.write(f'(Punctuator,{self.current_char},{self.position.line+1})?')
            return Token('Punctuator', self.current_char, self.position.line+1)


def run(fileName):
    # First we clear all tokens that is present in the file before
    open(r'./token.txt','w').close()

    #we append new tokens now 
    OpenFile = open(r'./code.txt','r')

    ReadFile = OpenFile.read()

    ObjectLexical = lexeical(fileName, ReadFile)

    Tokens , error = ObjectLexical.createTokens()
    
    # Placing End marker at the end
    OpenFile = open(r'./token.txt','a')
    OpenFile.write(f'(EndMarker,@,-)?')
    return Tokens, error


Tokens, error= run("./code.txt")
print(" Tokens:  ",Tokens,"\n Errors :  ",error)        





