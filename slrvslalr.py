import os
import ply.yacc as yacc
import ply.lex as lex

#================= LEXER ==============================================
#  ____________________________________________________________________
# |                                                                    |
# | Nesse ponto, são definidos os tokens e suas expressões regulares.  |
# |____________________________________________________________________|

# lista de tokens
tokens = (
'EQUAL',
'TIMES',
'ID'
)

# Expressões regulares
t_EQUAL   = r'='
t_TIMES   = r'\*'
t_ID      = r'[A-z][A-z0-9]*'
t_ignore  = ' \t\n' #expressões a ignorar

# recuperação de falha
def t_error(t):
    print("Caracter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

# construindo o lexer
lexer = lex.lex()


#================= ANALISADOR SINTÁTICO ===============================
#  ____________________________________________________________________
# |                                                                    |
# | Aqui, são descritas as regras de produção da gramática.            |
# | Gramática:                                                         |
# |     S -> L = R | R                                                 |
# |     L -> *R | id                                                   |
# |     R -> L                                                         |
# |____________________________________________________________________|

# Definindo as regras para S
def p_S(p): 
    '''S : L EQUAL R
         | R '''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 2:
        p[0] = p[1]

# Definindo as regras para L
def p_L(p):
    '''L : TIMES R
         | ID '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        p[0] = p[1]

# Definindo as regras para R
def p_R(p):
    'R : L'
    p[0] = p[1]

# Recuperação de falha na sintaxe
def p_error(p):
    print("Erro de sintaxe na entrada!")


#================= TABELAS DE PARSING =================================
#  ____________________________________________________________________
# |                                                                    |
# | Aqui é chamado o método yacc(), que recebe 'method' como parâmetro |
# | e gera dois arquivos de saída: parsertab.py e parser.out.          |
# |____________________________________________________________________|


#removendo arquivos antigos
try:
    os.remove("parserLALR.out")
    os.remove("parsetabLALR.py")
    os.remove("parserSLR.out")
    os.remove("parsetabSLR.py")
except:
    print()

#construindo o parser LALR
parserLALR = yacc.yacc(method='LALR')

#renomeando os arquivos para LALR
os.rename("parser.out", "parserLALR.out")
os.rename("parsetab.py", "parsetabLALR.py")

#construindo o parser SLR
parserSLR = yacc.yacc(method='SLR')

#renomeando os arquivos para SLR
os.rename("parser.out", "parserSLR.out")
os.rename("parsetab.py", "parsetabSLR.py")