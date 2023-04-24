import ply.yacc as yacc
import ply.lex as lex




# #Dictionary in which blockchains will be stored
blockData = {}


tokens = ['ID','BLOCK','ADD','PRINT','VIEW','RUN','MINE','EXPORT','STR','INT','LONG','FLOAT','LIST','TUPLE','DICT','NUM','ASSIGN','TYPEASSIGN','SEPARATOR','LPAREN','RPAREN','NE','LT',
          'GT', 'PCT', 'LE','GE','PLUS','MINUS','STAR','SLASH']

keywords = ['var', 'add', 'print', 'view', 'run', 'mine', 'export', 'str', 'int', 'long', 'float', 'List', 'Tuple', 'Dict','argsopt','test','args']

t_PLUS = r'\+'
t_MINUS = r'\-'
t_STAR = r'\*'
t_SLASH = r'\/'
t_PCT = r'\%'
t_ASSIGN = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NE = r'\!='
t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_SEPARATOR = r'\,'
t_TYPEASSIGN = r'\:'

#Building Parser
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH', 'PCT'),
)


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = t.value.upper()
    else:
        t.type = 'ID'
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_WHITESPACE(t):
    r'[ \t\r\n]+'
    t.lexer.lineno += len(t.value.count('\n'))
t_ignore = " \t\r\n"

# def t_EMPTY(t):
#     r'empty'
#     return t

def t_BLOCK(t):
    r'block'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_VAR(t):
    r'var'
    return t

def t_ADD(t):
    r'add'
    return t


def t_DICT(t):
    r'Dict'
    return t

def t_TUPLE(t):
    r'Tuple'
    return t

def t_LIST(t):
    r'List'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_INT(t):
    r'int'
    return t

def t_STR(t):
    r'str'
    return t

def t_EXPORT(t):
    r'export'
    return t

def t_MINE(t):
    r'mine'
    return t

def t_RUN(t):
    r'run'
    return t

def t_VIEW(t):
    r'view'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build Lexer

lexer = lex.lex()

def p_expr(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term'''
    
    # must check if expression is either 1 or 3
    # else throw exception

        # if only one term
    if len(p) == 2:
        p[0] = p[1]

    else:
        if len(p) == 4:
            if p[2] == '+':
                p[0] = p[1] + p[3]
            elif p[2] == '-':
                p[0] = p[1] - p[3]
            else:
                # must give an invalid error expression
                print("Invalid expr")
        # Invalid amount of terms
        
        
def p_term(p):
    '''term : factor
            | term STAR factor
            | term SLASH factor
            | term PCT factor'''
    

    # must check if expression is either 1 or 3
    # else throw exception
    
    if len(p) == 2:
        p[0] = p[1]
        
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        
        elif p[2] == '%':
            p[0] = p[1] % p[3]
            
        else:
            print("Invalid Expression")
    
def p_factor(p):
    '''factor : ID
              | NUM
              | LPAREN expression RPAREN
              | factor LPAREN argsopt RPAREN'''
           
              
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 4:
        p[0] = p[2]

    else:
        pass

def p_type(p):
    '''type : STR
            | INT
            | LONG
            | FLOAT
            | LIST
            | TUPLE
            | DICT'''
    p[0] = p[1]

def p_attribute(p):
    'attribute : ID TYPEASSIGN type'
    p[0] = (p[1], p[3])

def p_attributes(p):
    '''attributes : attribute
                  | attributes SEPARATOR attribute'''

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]
        
        
    


def p_new_att(p):
    '''new_att : ID TYPEASSIGN STR
               | ID TYPEASSIGN NUM'''
       
    p[0] = (p[1], p[3])


def p_new_atts(p):
    '''new_atts : new_att
                | new_atts SEPARATOR new_att'''
    

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


# #List of valid attributes:
validAttributes = ['STR','PLUS','MINUS','STAR','SLASH','PCT']

def p_block(p):
    'block : BLOCK ID'
    # '''block : BLOCK ID ASSIGN LPAREN attributes RPAREN
    #          | ADD ID ASSIGN LPAREN attributes RPAREN
    #          | PRINT ID
    #          | RUN ID
    #          | MINE ID
    #          | EXPORT ID
    #          | VIEW ID'''
    
    if (len(p) == 2):
        print("Created block")
        
    
    if len(p) == 7:
        for att in p[5]:
            if att not in validAttributes:
                print("Error in attributes")
                return False
            
                    
        if p[1] == 'BLOCK':
            print("Blockchain was created")
            return True
        
        elif p[1] == 'ADD':
            pass
        
        else:
            print("Blockchain could not be created")
            return False

    else:
        if p[1] == 'PRINT':
             print("Printing Block")
        elif p[1] == 'RUN':
             print("Running Block")
        elif p[1] == 'MINE':
             print("Minning Block")
        elif p[1] == 'EXPORT':
             print("Exporting Block")
        else:
             print("Viewing Block")
             

def p_test(p):
    '''test : expression NE expression
            | expression LT expression
            | expression LE expression
            | expression GE expression
            | expression GT expression'''
    
            
    if p[2] == '!=':
        p[0] = p[1] != p[3]

    elif p[2] == '<':
        p[0] = p[1] < p[3]

    elif p[2] == '<=':
        p[0] = p[1] <= p[3]

    elif p[2] == '>=':
        p[0] = p[1] >= p[3]

    elif p[2] == '>':
        p[0] = p[1] > p[3]
    
    else:
        print("Invalid Expression")
        

def p_argsopt(p):
    '''argsopt : args
               | empty'''
    pass

def p_args(p):
    '''args : expression SEPARATOR args
            | expression'''
    pass

def p_empty(p):
    'empty :'
    pass

# def p_error(p):
#     print("Syntax error in input")
    


parser = yacc.yacc()
# result = parser.parse('block MyBlock = (param1:str, param2:int)')
result = parser.parse('block myBlock')
print(result)  # Output: block was created



# block MyBlock = (param1:str, param2:int)
# add MyBlock = (param1:"First time!",param2:25)
# mine MyBlock
# print MyBlock
# Myval != 2 + 35





