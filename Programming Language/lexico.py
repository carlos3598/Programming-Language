import ply.lex as lex
import sys
# LEXER
# ==================================================================================
# ==================================================================================


# Reserved words
reserved = {
	'si' : 'SI',
	'sino': 'SINO',
	'mientras' : 'MIENTRAS',
	'desde': 'DESDE',
	'imprimir' : 'IMPRIMIR',
	'leer': 'LEER',
	'entero' : 'ENTERO',
	'flotante': 'FLOTANTE',
	'texto': 'TEXTO',
	'boleano' : 'BOLEANO',
	'vacio': 'VACIO',
	'nulo': 'NULO',
	'clase' : 'CLASE',
	'publico': 'PUBLICO',
	'privado' : 'PRIVADO',
	'agregar' : 'AGREGAR',
	'remover': 'REMOVER',
	'insertar' : 'INSERTAR',
	'vaciar': 'VACIAR',
	'obtener' : 'OBTENER',
	'programa': 'PROGRAMA',
	'regresa' : 'REGRESA',
	'verdadero': 'VERDADERO',
	'falso' : 'FALSO',
	'y': 'Y',
	'o': 'O',
	'lista': 'LISTA',
}


# List of tokens
tokens = ['ID','CTE_TEXTO','CTE_ENTERO','CTE_FLOTANTE'] + list(reserved.values())


# String Regex
t_CTE_TEXTO 	= r'\"(\\.|[^"])*\"'
t_CTE_FLOTANTE 	= r'[0-9]+[.][0-9]+'
t_CTE_ENTERO	= r'[0-9]+'


# Literals Regex
literals = "-+*/;,.:{}[]=()><%!"


# Function Regex
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value,'ID')
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("line %d, lexical error: Illegal character '%s'" % (t.lexer.lineno, t.value[0]))
    sys.exit()
