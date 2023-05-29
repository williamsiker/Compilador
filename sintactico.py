import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin
from semantico import *

precedence = (
    ('right', 'ID'),
    ('right', 'ASIGNAR'),
    ('left', 'LPARENT', 'RPARENT')
)


def p_block(p):
    '''block : statement_list'''
    p[0] = block(p[1], "block")
    # print("block")


def p_statement_list1(p):
    '''statement_list : statement statement_list'''
    p[0] = statement_list1(p[1],p[2], "statement_list")
    # print("statement_list", p[1]) #1 hijo

def p_statement_list2(p):
    '''statement_list : statement'''
    p[0] = statement_list2(p[1], "statement_list")
    # print("statement_list", p[1]) #1 hijo

def p_statement(p):
    '''statement : crearventana FINL
    			 | crearframe FINL
                 | crearboton FINL
                 | crearetiqueta FINL
                 | iniciar FINL'''

    p[0] = statement(p[1], "statement")
    print("statement", p[1], p[2])  # dos hijos


def p_crearventana(p):
    '''crearventana : ID ASIGNAR CREARVENTANA LPARENT RPARENT'''
    p[0] = crearventana(Id(p[1]), Assign(p[2]), Ventana(p[3]), "crearventana")
    print("crearventana", p[1])


def p_crearframe(p):
    '''crearframe : ID ASIGNAR CREARFRAME LPARENT argument_list RPARENT'''
    p[0] = crearframe(Id(p[1]), Assign(p[2]), Ventana(p[3]), p[5], "crearframe")
    print("crear frame", p[1])


def p_crearboton(p):
    '''crearboton : ID ASIGNAR CREARBOTON LPARENT argument_list RPARENT'''
    p[0] = crearboton(Id(p[1]), Assign(p[2]), Ventana(p[3]), p[5], "creaboton")
    print("creando boton", p[1])


def p_crearetiqueta(p):
    '''crearetiqueta : ID ASIGNAR CREARETIQUETA LPARENT argument_list RPARENT'''
    p[0] = crearetiqueta(Id(p[1]), Assign(p[2]), Ventana(p[3]), p[5], "crearetiqueta")
    print("Crear etiqueta", p[1])


def p_iniciar(p):
    '''iniciar : ID DOT INICIAR LPARENT RPARENT'''
    p[0] = iniciar(Id(p[1]), Ventana(p[3]), "Iniciar")
    print("Inciando ventana")


def p_argument_list1(p):
    '''argument_list : argument'''
    p[0] = argument_list1(p[1], "argument_list1")
    print("argument_list", p[1])

def p_argument_list2(p):
    '''argument_list : argument COMA argument_list'''
    p[0] = argument_list2(p[1], p[3],"argument_list2")
    print("argument_list", p[1])


def p_argument1(p):
    '''argument : ID'''
    p[0] = argument1(Id(p[1]), "argument1")
    print("argument", p[1])

def p_argument2(p):
    '''argument : TEXT'''
    p[0] = argument2(Id(p[1]), "argument2")
    print("argument", p[1])


def p_error(p):
    print("Error de sintaxis ", p)


# print "Error en la linea "+str(p.lineno)


# test = 'test\prueba.txt'
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

# parser = yacc.yacc()
# result = parser.parse(cadena,debug=0)
# print(result) 

def traducir(result):
    graphFile = open('arbol.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print("El programa traducido se guardo en \"arbol.vz\"")


test = 'test\prueba.txt'
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena)

result.imprimir(" ")
#traducir(result)