import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['CREARVENTANA', 'CREARFRAME', 'CREARBOTON', 'CREARETIQUETA',
              'INICIAR']

tokens = reservadas + ['ID', 'TEXT', 'NUMBER', 'ASIGNAR', 'COMA',
                       'FINL', 'DOT', 'LPARENT', 'RPARENT']

# tokens = ['ID', 'NUMBER', 'ASIGNAR', 'COMA',
#         'FINL', 'DOT', 'LPARENT', 'RPARENT'
# 		]

# reservadas = {
#     'crearventana':'CREARVENTANA',
#     'crearframe':'CREARFRAME',
#     'crearboton':'CREARBOTON',
#     'crearetiqueta':'CREARETIQUETA'
# }

#tokens = tokens+list(reservadas.values())

t_ignore = '\t '
t_ASIGNAR = r'='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMA = r','
t_FINL = r'°'
t_DOT = r'\.'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        # reservadas.get(t.value,'ID')
        t.type = t.value

    return t

def t_TEXT(t):
    r"'[a-zA-Z_][a-zA-Z0-9_]*'"
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        # reservadas.get(t.value,'ID')
        t.type = t.value

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ccode_nonspace(t):
    r'\s+'
pass


# dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
    r'\#.*'
    pass


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

'''
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print
        str(cont) + ". " + file
        cont = cont + 1

    while respuesta == False:
        numArchivo = raw_input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print
    "Has escogido \"%s\" \n" % files[int(numArchivo) - 1]

    return files[int(numArchivo) - 1]
'''

# test = 'test\prueba.txt'
# fp = codecs.open(test, "r", "utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

# analizador.input(cadena)

# while True:
#     tok = analizador.token()
#     if not tok: break
#     print (tok)