"""
Autores:

	Alberto Chapa 	A01138418
	Carlos Salazar 	A00809015
"""
import sys
import ply.lex as lex
import re

# LEXER
# ==================================================================================
# ==================================================================================
# Reserved words
reserved = {
	'si' : 'SI',
	'sino': 'SINO',
	'mientras' : 'MIENTRAS',
	'imprimir' : 'IMPRIMIR',
	'imprimirSalto' : 'IMPRIMIRSALTO',
	'leer': 'LEER',
	'entero' : 'ENTERO',
	'flotante': 'FLOTANTE',
	'texto': 'TEXTO',
	'boleano' : 'BOLEANO',
	'vacio': 'VACIO',
	'nulo': 'NULO',
	'clase' : 'CLASE',
	'publico': 'PUBLICO',
	'programa': 'PROGRAMA',
	'regresa' : 'REGRESA',
	'verdadero': 'VERDADERO',
	'falso' : 'FALSO',
	'y': 'Y',
	'o': 'O',
	'funcion' : 'FUNCION',
}

# List of tokens
tokens = ['ID','CTE_TEXTO','CTE_ENTERO','CTE_FLOTANTE', 'LE', 'GE', 'EQ', 'NEQ'] + list(reserved.values())

# String Regex
t_CTE_TEXTO 	= r'\"(\\.|[^"])*\"'
t_CTE_FLOTANTE 	= r'[0-9]+[.][0-9]+'
t_CTE_ENTERO	= r'[0-9]+'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='

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

lexer = lex.lex()





# MAQUINA VIRTUAL
# ==================================================================================
# ==================================================================================
import virtualMachine

# CUBO
# ==================================================================================
# ==================================================================================
import cubo

# MapaMemoria
# ==================================================================================
# ==================================================================================
from MapaMemoria import MapaMemoria
mapa = MapaMemoria()

# PARSER
# ==================================================================================
# ==================================================================================
tablaProcedimientos = []
tablaVariables = []
dictClases = {}

scope = ""
scopeClase = ""
tipoVar = ""
nombreFuncion = ""
pilaO = []
pOper = []
pTipo = []
cuadruplos = []
countTemp = 0
tipoAsignacion = ""
idAsignacion = ""
pSaltos = []
countParameter = 0
varcteId = ""
varcteIdIsFunc = False
varcteIdIsVector = False
tempNombreFunc = ""
varBoundAsign = 0
dirBaseVector = 0
idAsignIsVector = False
tempNombreVector = ""
isTypeClass = False
idAssignIsAttr = False
varcteIdIsAttr = False
escrituraType = ""
isClassMethodCall = False
idAsignLlamadaFunc = ""
className = ""
afterDotId = ""


dictVirtualDirs = {
	'globalInt' : 10000,
	'globalFloat' : 20000,
	'globalTexto' : 30000,
	'globalBoleano' : 40000,

	'localInt' : 50000,
	'localFloat' : 60000,
	'localTexto' : 70000,
	'localBoleano' : 80000,

	'tempInt' : 90000,
	'tempFloat' : 100000,
	'tempTexto' : 110000,
	'tempBoleano' : 120000,

	'consInt' : 130000,
	'consFloat' : 140000,
	'consTexto' : 150000,
	'consBoleano' : 160000
}

staticDirVirtual = {
	'globalInt' : 10000,
	'globalFloat' : 20000,
	'globalTexto' : 30000,
	'globalBoleano' : 40000,

	'localInt' : 50000,
	'localFloat' : 60000,
	'localTexto' : 70000,
	'localBoleano' : 80000,

	'tempInt' : 90000,
	'tempFloat' : 100000,
	'tempTexto' : 110000,
	'tempBoleano' : 120000,

	'consInt' : 130000,
	'consFloat' : 140000,
	'consTexto' : 150000,
	'consBoleano' : 160000
}


import ply.yacc as yacc

def p_programa(p):
	'''programa : firstQuadruple clases scopeGlobal vars funciones PROGRAMA scopePrograma bloque'''
	print("Programa correcto\n")
	print("Tabla de Variables:")
	for i in tablaVariables:
		print(i[0] + " " + i[1] + " " + i[2] + " " + str(i[3]) + " " + str(i[4]) )
	print()
	print("Tabla de Procedimientos:")
	print (tablaProcedimientos)
	print()
	#print("pila de Tipo:")
	#print(pTipo)
	#print("pila de Operandos:")
	#print(pilaO)
	print("cuadruplos")
	for i in cuadruplos:
		print(i)
	print()
	print("Current Map")
	print(mapa.hashMM)
	print()
	print("Tabla de Clases")
	print(dictClases)
	virtualMachine.virtualMachine(cuadruplos,mapa,staticDirVirtual,tablaProcedimientos,tablaVariables)


def p_firstQuadruple(p):
	'''firstQuadruple : '''
	global cuadruplos
	cuadruplos.append(["goto", "" ,"", None])


def p_clases(p):
	'''clases : clase clases
			  |'''


def p_scopeGlobal(p):
	'scopeGlobal : '
	global scope
	scope = "global"


def p_scopePrograma(p):
	'scopePrograma : '
	global scope, cuadruplos
	scope = "programa"
	cuadruplos[0][3] = len(cuadruplos)


def p_vars(p):
	'''vars : var vars
			|'''

def p_funciones(p):
	'''funciones : funcion funciones
			     |'''


def p_var(p):
	'''var : tipo varNombre varsVector var2 ';' '''
	global isTypeClass
	isTypeClass = False


def p_varsVector(p):
	'''varsVector : '[' CTE_ENTERO ']'
				  |'''
	if len(p) > 1:
		updateVarSize(int(p[2]))


def p_var2(p):
	'''var2 : ',' varNombre varsVector var2
		     |'''

def p_varNombre(p):
	'''varNombre : ID'''
	agregarVariable(p[1])


def p_funcion(p):
	'''funcion : FUNCION tipo nombreFuncion '(' metodo2 agregaFirma bloque'''
	global scope, cuadruplos
	scope = ""
	cuadruplos.append(["retornoLinea","","",""])

def p_nombreFuncion(p):
	'''nombreFuncion : ID'''
	global scope, nombreFuncion, tablaProcedimientos
	scope = p[1]
	nombreFuncion = p[1]
	agregaProcedimiento()

def p_agregaFirma(p):
	'''agregaFirma : ')' '''
	firmaProcedimiento()

def p_tipo(p):
	'''tipo : ENTERO
			| FLOTANTE
			| TEXTO
			| BOLEANO
			| checkClassExistance
			| VACIO'''
	global tipoVar
	if not isTypeClass:
		tipoVar = p[1]


def p_checkClassExistance(p):
	'''checkClassExistance : ID'''
	global isTypeClass, tipoVar
	isTypeClass = True
	tipoVar = p[1]
	if not tipoVar in dictClases:
		print("La clase " + tipoVar + " no esta definida")
		sys.exit()




def p_bloque(p):
	'''bloque : '{' bloque1 '}' '''


def p_bloque1(p):
	'''bloque1 : estatuto bloque1
			   |'''

def p_estatuto(p):
	'''estatuto : catchIdAsignacionOrLlamadaFunc asignacionOrLlamadaFunc
				| condicion
				| escritura
				| ciclowhile
				| lectura
				| var
				| metodo5'''


def p_catchIdasignacionOrLlamadaFunc(p):
	'''catchIdAsignacionOrLlamadaFunc : ID nextIde'''
	global idAsignLlamadaFunc
	idAsignLlamadaFunc = p[1]


def p_nextIde(p):
	'''nextIde : '.' ID
			   |'''
	global afterDotId
	if len(p) > 1:
		afterDotId = p[2]

def p_asignacionOrLlamadaFunc(p):
	'''asignacionOrLlamadaFunc : llamadaFuncion
						       | asignacion'''


def p_llamadaFuncion(p):
	'''llamadaFuncion : verificarProc parametrosLlamada ')' ';' '''
	global cuadruplos, pTipo, pilaO, afterDotId

	absFuncName = ""
	if afterDotId != "":
		absFuncName = afterDotId
		llamadaFuncionActions(afterDotId,className)
	else:
		absFuncName = idAsignLlamadaFunc
		llamadaFuncionActions(idAsignLlamadaFunc,"global")

	newDirTemp = 0
	funcType = -1;
	for i in tablaProcedimientos:
		if i[0] == absFuncName:
			funcType = i[3]
			newDirTemp = regresaTempDirVirtual(funcType)
			break
	cuadruplos.append(["asignRetFuncValue",newDirTemp,"",""])
	pilaO.append(newDirTemp)
	pTipo.append(funcType)
	afterDotId = ""


def p_verificarProc(p):
	'''verificarProc : '(' '''
	global className
	if afterDotId == "":
		existenciaProc(idAsignLlamadaFunc)
	else:
		exists = False
		for i in tablaVariables:
			if i[0] == idAsignLlamadaFunc:
				className = i[1]
				exists = True
				break

		if not exists:
			print("La variable " + idAsignLlamadaFunc + " no existe")
			sys.exit()

		exists = False
		for i in tablaProcedimientos:
			if i[0] == afterDotId and i[1] == className:
				exists = True
				break

		if not exists:
			print("La clase " + className + " no tiene el metodo " + afterDotId)
			sys.exit()

		cuadruplos.append(["era", afterDotId, scope, className])


def p_parametrosLlamada(p):
	'''parametrosLlamada : expresion parametrosLlamada2
						 | '''
	global countParameter
	if len(p) > 1:
		countParameter = countParameter + 1



def p_parametrosLlamada2(p):
	'''parametrosLlamada2 : ',' expresion parametrosLlamada2
						 |'''
	global 	countParameter
	if len(p) > 1:
		countParameter = countParameter + 1


def p_asignacion(p):
	'''asignacion : revisaQueExistaID asignacion1 '=' expresion ';' '''
	global cuadruplos, pilaO, pTipo, idAsignIsVector, idAssignIsAttr, mapa, afterDotId

	operandoToAsign = pilaO.pop()
	tipoToAsign = pTipo.pop()
	operandoToBeAsigned = dirBaseVector
	tipoToBeAsigned = matchTipo(tipoAsignacion)
	idAsignMark = 0

	if idAsignIsVector or idAssignIsAttr:
		if idAsignIsVector:
			idAsignMark = 1
		operandoToBeAsigned = pilaO.pop()
		tipoToBeAsigned = pTipo.pop()

	if cubo.cuboSemantico[tipoToBeAsigned][tipoToAsign][regresaOperacion("=")] < 0:
		print("Asignacion invalida de tipos.")
		sys.exit()

	cuadruplos.append([regresaOperacion("="), operandoToAsign, idAsignMark, operandoToBeAsigned])
	idAsignIsVector = False
	idAssignIsAttr = False
	afterDotId = ""


def p_revisaQueExistaID(p):
	'''revisaQueExistaID : '''
	global scopeClase, idAsignacion, tipoAsignacion, varBoundAsign, dirBaseVector, pilaO, pTipo, idAssignIsAttr
	
	exists = False;
	#checo locales
	for i in tablaVariables:
		if i[0] == idAsignLlamadaFunc and i[2] == scopeClase + scope:
			exists = True
			idAsignacion = i[0]
			tipoAsignacion = i[1]
			varBoundAsign = i[4]
			dirBaseVector = i[3]
			break

	#checo globales
	if not exists:
		funcScope = "global" if scopeClase == "" else scopeClase
		for i in tablaVariables:
			if i[0] == idAsignLlamadaFunc and i[2] == funcScope:
				exists = True
				idAsignacion = i[0]
				tipoAsignacion = i[1]
				varBoundAsign = i[4]
				dirBaseVector = i[3]
				break

	if not exists:
		print("La variable " + idAsignLlamadaFunc +" no ha sido declarada ")
		sys.exit()

	if afterDotId != "":
		idAssignIsAttr = True
		attrDir = 0
		attrType = ""
		for i in tablaVariables:
			if i[0] == idAsignacion:
				attrDir = i[3][afterDotId][0]
				attrType = i[3][afterDotId][1]
				break

		pilaO.append(attrDir)
		pTipo.append(attrType)


def p_asignacion1(p):
	'''asignacion1 : vectorAsignacion
				   |'''


def p_vectorAsignacion(p):
	'''vectorAsignacion : '[' exp ']' '''
	verificaVectorAsignacion()


def p_escritura(p):
	'''escritura : escrituraType '(' expresion ')' ';' '''
	global cuadruplos, idAsignacion, pilaO, pTipo
	cuadruplos.append([escrituraType, "", "", pilaO.pop()])
	pTipo.pop()


def p_escrituraType(p):
	'''escrituraType : IMPRIMIR
					 | IMPRIMIRSALTO'''
	global escrituraType
	escrituraType = p[1]


def p_condicion(p):
	'''condicion : SI '(' superexpresion leftParentesisCondicion bloque condicion1'''
	global cuadruplos, pSaltos
	fin = pSaltos.pop()
	cuadruplos[fin][3] = len(cuadruplos)

def p_leftParentesisCondicion(p):
	'''leftParentesisCondicion : ')' '''
	parentesisDer()

def p_condicion1(p):
	'''condicion1 : sinoCondicion bloque
				  |'''

def p_sinoCondicion(p):
	'''sinoCondicion : SINO'''
	global cuadruplos, pSaltos
	cuadruplos.append(["goto", "" , "" , None])
	falso = pSaltos.pop()
	pSaltos.append(len(cuadruplos) - 1)
	cuadruplos[falso][3] = len(cuadruplos)


def p_lectura(p):
	'''lectura : LEER '(' revisaQueExistaID ')' ';' '''
	global cuadruplos, idAsignacion
	cuadruplos.append(["leer", "", "", idAsignacion])

def p_ciclowhile(p):
	'''ciclowhile : MIENTRAS parentesisIzqWhile superexpresion parentesisDerWhile bloque'''
	global cuadruplos, pSaltos
	falso = pSaltos.pop()
	retorno = pSaltos.pop()
	cuadruplos.append(["goto", "" , "" , retorno])
	cuadruplos[falso][3] = len(cuadruplos)

def p_parentesisIzqWhile(p):
	'''parentesisIzqWhile : '(' '''
	global cuadruplos
	pSaltos.append(len(cuadruplos))

def p_parentesisDerWhile(p):
	'''parentesisDerWhile : ')' '''
	parentesisDer()



def p_superexpresion(p):
	'''superexpresion : expresion checaSuperExpresion superexpresion1'''

def p_checaSuperExpresion(p):
	'''checaSuperExpresion :'''
	global pTipo, pOper

	if len(pOper) > 0 and (pOper[len(pOper) - 1] == 'y' or pOper[len(pOper) - 1] == 'o'):
		tipo1 = pTipo.pop()
		tipo2 = pTipo.pop()
		operando = pOper.pop()
		num1 = pilaO.pop()
		num2 = pilaO.pop()
		IsExpValid = cubo.cuboSemantico[tipo1][tipo2][regresaOperacion(operando)]
		if IsExpValid < 0:
			print("Operacion no valida. " + num2 + operando + num1)
			sys.exit()
		dirtemp = regresaTempDirVirtual(IsExpValid)
		cuadruplos.append([regresaOperacion(operando), num2, num1, dirtemp])
		pilaO.append(dirtemp)
		pTipo.append(IsExpValid)

def p_superexpresion1(p):
	'''superexpresion1 : operationSuperExpresion superexpresion
					   |'''

def p_operationSuperExpresion(p):
	'''operationSuperExpresion : Y
							   | O'''
	global pOper
	pOper.append(p[1])

def p_expresion(p):
	'''expresion : exp expresion1'''


def p_expresion1(p):
	'''expresion1 : '>' exp
				  | GE exp
				  | '<' exp
				  | LE exp
				  | NEQ exp
				  | EQ exp
				  |'''

	global pTipo, pOper
	if len(p) > 1:
		pOper.append(p[1])
	if len(p) > 1 and len(pOper) > 0 and pOper[len(pOper) - 1] == p[1]:
		tipo1 = pTipo.pop()
		tipo2 = pTipo.pop()
		operando = pOper.pop()
		num1 = pilaO.pop()
		num2 = pilaO.pop()
		IsExpValid = cubo.cuboSemantico[tipo1][tipo2][regresaOperacion(operando)]
		if IsExpValid < 0:
			print("Operacion no valida. " + str(num2) + operando + str(num1))
			sys.exit()
		dirtemp = regresaTempDirVirtual(IsExpValid)
		cuadruplos.append([regresaOperacion(operando), num2, num1, dirtemp])
		pilaO.append(dirtemp)
		pTipo.append(IsExpValid)

def p_exp(p):
	'''exp : termino checaExp exp1'''

def p_checaExp(p):
	'''checaExp : '''
	global pTipo, pOper, mapa

	if len(pOper) > 0 and (pOper[len(pOper) - 1] == '+' or pOper[len(pOper) - 1] == '-'):
		tipo1 = pTipo.pop()
		tipo2 = pTipo.pop()
		operando = pOper.pop()
		num1 = pilaO.pop()
		num2 = pilaO.pop()
		IsExpValid = cubo.cuboSemantico[tipo1][tipo2][regresaOperacion(operando)]
		if IsExpValid < 0:
			print("Operacion no valida. " + num2 + operando + num1)
			sys.exit()
		dirtemp = regresaTempDirVirtual(IsExpValid)
		cuadruplos.append([regresaOperacion(operando), num2, num1, dirtemp])
		mapa.hashMM[dirtemp] = 0
		pilaO.append(dirtemp)
		pTipo.append(IsExpValid)

def p_exp1(p):
	'''exp1 : operationExp exp
	        |'''

def p_operationExp(p):
	'''operationExp : '+'
					| '-' '''
	global pOper
	pOper.append(p[1])

def p_termino(p):
	'''termino : factor checaTermino termino1'''


def p_termino1(p):
	'''termino1 : operationTermino termino
				|'''

def p_checaTermino(p):
	'''checaTermino : '''
	global pTipo, pOper

	if len(pOper) > 0 and (pOper[len(pOper) - 1] == '*' or pOper[len(pOper) - 1] == '/' or pOper[len(pOper) - 1] == '%'):
		tipo1 = pTipo.pop()
		tipo2 = pTipo.pop()
		operando = pOper.pop()
		num1 = pilaO.pop()
		num2 = pilaO.pop()
		IsExpValid = cubo.cuboSemantico[tipo1][tipo2][regresaOperacion(operando)]
		if IsExpValid < 0:
			print("Operacion no valida. " + num2 + operando + num1)
			sys.exit()
		dirtemp = regresaTempDirVirtual(IsExpValid)
		cuadruplos.append([regresaOperacion(operando), num2, num1, dirtemp])
		pilaO.append(dirtemp)
		pTipo.append(cubo.cuboSemantico[tipo1][tipo2][regresaOperacion(operando)])


def p_operationTermino(p):
	'''operationTermino : '*'
					   | '/'
					   | '%' '''
	global pOper
	pOper.append(p[1])

def p_factor(p):
	'''factor : parentesisIzq superexpresion parentesisDer
			  | operationFactor varcte
			  | varcte'''

def p_parentesisIzq(p):
	'''parentesisIzq : '(' '''
	global pOper
	pOper.append('(')

def p_parentesisDer(p):
	'''parentesisDer : ')' '''
	global pOper
	pOper.pop()

def p_operationFactor(p):
	'''operationFactor : '+'
					   | '-' '''



def p_varcte(p):
	'''varcte : varcteID
			  | constantes
			  | NULO'''

def p_constantes(p):
	'''constantes :	CTE_ENTERO
				  | CTE_FLOTANTE
				  | CTE_TEXTO
				  | VERDADERO
				  | FALSO'''
	meterAPila(p[1])

def p_varcteID(p):
	'''varcteID : guardarVarcteId varct'''
	global varcteIdIsFunc, varcteIdIsVector, varcteIdIsAttr
	if not varcteIdIsFunc and not varcteIdIsVector and not varcteIdIsAttr:
		meterAPila(varcteId)
	varcteIdIsFunc = False
	varcteIdIsVector = False
	varcteIdIsAttr = False

def p_guardarVarcteId(p):
	'''guardarVarcteId : ID'''
	global varcteId
	varcteId = p[1]

def p_varct(p):
	'''varct : varcte1
			 | varcte2
			 | vectorExp
			 | '''


def p_varcte1(p):
	'''varcte1 : '.' ID'''
	global varcteIdIsAttr, pTipo, pilaO
	varcteIdIsAttr = True

	attr = 0
	attrType = -1
	exists = False
	for i in tablaVariables:
		if i[0] == varcteId and i[2] == scope:
			attr = i[3][p[2]][0]
			attrType = i[3][p[2]][1]
			exists = True
			break

	if not exists:
		for i in tablaVariables:
			if i[0] == varcteId and i[2] == "global":
				exists = True
				attr = i[3][p[2]][0]
				attrType = i[3][p[2]][1]
				break

	#No se encontro en la tabla de variables
	if not exists:
		print(varcteId + " no existe")
		sys.exit()

	pTipo.append(attrType)
	pilaO.append(attr)


def p_vectorExp(p):
	'''vectorExp : corcheteIzq saveTempNombreVector exp corcheteDer'''
	verificaVectorExp()

def p_saveTempNombreVector(p):
	'''saveTempNombreVector : '''
	global tempNombreVector
	tempNombreVector = varcteId


def p_corcheteIzq(p):
	'''corcheteIzq : '[' '''
	global pOper
	pOper.append('[')


def p_corcheteDer(p):
	'''corcheteDer : ']' '''
	global pOper
	pOper.pop()


def p_varcte2(p):
	'''varcte2 : parentesisIzq saveTempNombreFunc varcte3 parentesisDer '''
	global varcteIdIsFunc, cuadruplos, pilaO, pTipo
	varcteId = tempNombreFunc
	varcteIdIsFunc = True
	existenciaProc(varcteId)
	llamadaFuncionActions(varcteId,"global")

	newDirTemp = 0
	funcType = -1;
	for i in tablaProcedimientos:
		if i[0] == varcteId:
			funcType = i[3]
			newDirTemp = regresaTempDirVirtual(funcType)
			break
	cuadruplos.append(["asignRetFuncValue",newDirTemp,"",""])
	pilaO.append(newDirTemp)
	pTipo.append(funcType)


def p_saveTempNombreFunc(p):
	'''saveTempNombreFunc : '''
	global tempNombreFunc
	tempNombreFunc = varcteId


def p_varcte3(p):
	'''varcte3 : exp varcte4
	           |'''
	global countParameter
	if len(p) > 1:
		countParameter = countParameter + 1


def p_varcte4(p):
	'''varcte4 : ',' exp varcte4
	           |'''
	global 	countParameter
	if len(p) > 1:
		countParameter = countParameter + 1


def p_clase(p):
	'''clase : CLASE nombreClase clase1 '{' public '}' ';' '''
	global scopeClase
	scopeClase = ""

def p_nombreClase(p):
	'''nombreClase : ID'''
	global scopeClase, dictClases
	scopeClase = p[1]
	dictClases[p[1]] = 1;

def p_clase1(p):
	'''clase1 : ':' ID
			  |'''

def p_public(p):
	'''public : PUBLICO ':' vars funciones
			  |'''

def p_metodo2(p):
	'''metodo2 : tipo nombreParametro metodo21
			   |'''

def p_metodo21(p):
	'''metodo21 : ',' tipo nombreParametro metodo21
				| '''

def p_nombreParametro(p):
	'''nombreParametro : ID'''
	agregarVariable(p[1])


def p_metodo5(p):
	'''metodo5 : REGRESA expresion ';' '''
	global cuadruplos, pilaO
	if tipoVar == "vacio":
		print("Error: La funcion es vacía y no debe regresar ningun valor.")
		sys.exit()

	returnType = pTipo.pop()
	if returnType != matchTipo(tipoVar):
		print("Error: La funcion no regresa el tipo correcto.")
		sys.exit()

	cuadruplos.append(["retornoValor",pilaO.pop(),"",""])




#=================================
#Metodos Externos
def agregarVariable(id):
	global tablaVariables, scopeClase

	for i in tablaVariables:
		if i[0] == id and i[2] == scopeClase + scope:
			print("Variable " + id + " ya declarada en el mismo scope")
			sys.exit()

	dirVirtual = None
	if isTypeClass:
		attrsDict = {}
		for j in tablaVariables:
			if j[2] == tipoVar:
				attrsDict[j[0]] = [createMemoryForVariable(j[1]),matchTipo(j[1])]
		dirVirtual = attrsDict
	else:
		dirVirtual = createMemoryForVariable(tipoVar)

	tablaVariables.append([id, tipoVar, scopeClase + scope, dirVirtual, 1])

def createMemoryForVariable(tipoVar):
	global dictVirtualDirs, mapa
	dirVirtual = 0
	if scope == "global":

		if tipoVar == "entero":
			dirVirtual = dictVirtualDirs['globalInt']
			dictVirtualDirs['globalInt'] = dictVirtualDirs['globalInt'] + 1
			mapa.hashMM[dirVirtual] = 0

		elif tipoVar == "flotante":
			dirVirtual = dictVirtualDirs['globalFloat']
			dictVirtualDirs['globalFloat'] = dictVirtualDirs['globalFloat'] + 1
			mapa.hashMM[dirVirtual] =  0.0

		elif tipoVar == "texto":
			dirVirtual = dictVirtualDirs['globalTexto']
			dictVirtualDirs['globalTexto'] = dictVirtualDirs['globalTexto'] + 1
			mapa.hashMM[dirVirtual] = ""

		elif tipoVar == "boleano":
			dirVirtual = dictVirtualDirs['globalBoleano']
			dictVirtualDirs['globalBoleano'] = dictVirtualDirs['globalBoleano'] + 1
			mapa.hashMM[dirVirtual] = "falso"
	else:
		if tipoVar == "entero":
			dirVirtual = dictVirtualDirs['localInt']
			dictVirtualDirs['localInt'] = dictVirtualDirs['localInt'] + 1
			mapa.hashMM[dirVirtual] = 0

		elif tipoVar == "flotante":
			dirVirtual = dictVirtualDirs['localFloat']
			dictVirtualDirs['localFloat'] = dictVirtualDirs['localFloat'] + 1
			mapa.hashMM[dirVirtual] =  0.0

		elif tipoVar == "texto":
			dirVirtual = dictVirtualDirs['localTexto']
			dictVirtualDirs['localTexto'] = dictVirtualDirs['localTexto'] + 1
			mapa.hashMM[dirVirtual] = ""

		elif tipoVar == "boleano":
			dirVirtual = dictVirtualDirs['localBoleano']
			dictVirtualDirs['localBoleano'] = dictVirtualDirs['localBoleano'] + 1
			mapa.hashMM[dirVirtual] = "falso"

	return dirVirtual

def agregaProcedimiento():
	global nombreFuncion, tablaProcedimientos, scopeClase
	firma = []
	funcScope = "global" if scopeClase == "" else scopeClase
	for i in tablaProcedimientos:
		if i[0] == nombreFuncion and i[1] == funcScope:
			print("La funcion " + nombreFuncion + ", ya ha sido declarada en el scope " + funcScope)
			sys.exit()
	tablaProcedimientos.append([nombreFuncion, funcScope, len(cuadruplos), matchTipo(tipoVar)])

def firmaProcedimiento():
	global nombreFuncion, tablaProcedimientos, scopeClase

	firma = []
	dirVariables = []
	for i in tablaVariables:
		if i[2] == scopeClase + nombreFuncion:
			firma.append(matchTipo(i[1]))
			dirVariables.append(i[3])
	tablaProcedimientos[len(tablaProcedimientos) - 1].append(firma)
	tablaProcedimientos[len(tablaProcedimientos) - 1].append(dirVariables)

def meterAPila(varcte):
	global pilaO, PTipo, dictVirtualDirs, mapa
	#Encontra el numero, flotante, texto o boleano en forma de constante
	if matchTipo(varcte) >= 0:
		consVirtual = 0
		if matchTipo(varcte) == 0:
			consVirtual = dictVirtualDirs['consInt']
			mapa.hashMM[consVirtual] = int(varcte)
			dictVirtualDirs['consInt'] = dictVirtualDirs['consInt'] + 1

		elif matchTipo(varcte) == 1:
			consVirtual = dictVirtualDirs['consFloat']
			mapa.hashMM[consVirtual] = float(varcte)
			dictVirtualDirs['consFloat'] = dictVirtualDirs['consFloat'] + 1

		elif matchTipo(varcte) == 2:
			consVirtual = dictVirtualDirs['consTexto']
			mapa.hashMM[consVirtual] = varcte.replace('"',"")
			dictVirtualDirs['consTexto'] = dictVirtualDirs['consTexto'] + 1

		elif matchTipo(varcte) == 3:
			consVirtual = dictVirtualDirs['consBoleano']
			mapa.hashMM[consVirtual] = varcte
			dictVirtualDirs['consBoleano'] = dictVirtualDirs['consBoleano'] + 1

		pilaO.append(consVirtual)
		pTipo.append(matchTipo(varcte))
	else:
		#Verifica si el id esta en la tabla de variables
		tipoVarcte = None
		exists = False
		for i in tablaVariables:
			if i[0] == varcte and i[2] == scopeClase + scope:
				tipoVarcte = i[1]
				pTipo.append(matchTipo(tipoVarcte))
				pilaO.append(i[3])
				exists = True
				break

		if not exists:
			globalScope = "global" if scopeClase == "" else scopeClase
			for i in tablaVariables:
				if i[0] == varcte and i[2] == globalScope:
					tipoVarcte = i[1]
					pTipo.append(matchTipo(tipoVarcte))
					if globalScope == "global":
						pilaO.append(i[3])
					else:
						pilaO.append(str(i[3])+'_'+i[0]+'#')
					exists = True
					break
		#No se encontro en la tabla de variables
		if not exists:
			print(varcte + " no existe")
			sys.exit()

def matchTipo(varcte):
	#Encontre flotante
	if re.match(r'[0-9]+[.][0-9]+', varcte) or varcte == "flotante":
		return 1
	#Encontre entero
	elif re.match(r'[0-9]+', varcte) or varcte =="entero":
		return 0
	#Encontre boleano
	#Encontre texto
	elif re.match(r'\"(\\.|[^"])*\"', varcte) or varcte == "texto":
		return 2
	#Encontre boleano
	elif varcte == 'verdadero' or varcte == 'falso' or varcte == "boleano":
		return 3
	#No encontre nada
	else:
		return -1

def parentesisDer():
	global pTipo, cuadruplos, pilaO, pSaltos
	if pTipo.pop() != 3: #checa si es boleano
		print("No se puede evaluar la condicion")
		sys.exit()
	resultado = pilaO.pop()
	cuadruplos.append(["gotoF", resultado, "" , None])
	pSaltos.append(len(cuadruplos) - 1)

def regresaTempDirVirtual(tipo):
	global dictVirtualDirs
	tempDir = 0
	if tipo == 0:
		tempDir = dictVirtualDirs['tempInt']
		dictVirtualDirs['tempInt'] = dictVirtualDirs['tempInt'] + 1
	elif tipo == 1:
		tempDir = dictVirtualDirs['tempFloat']
		dictVirtualDirs['tempFloat'] = dictVirtualDirs['tempFloat'] + 1
	elif tipo == 2:
		tempDir = dictVirtualDirs['tempTexto']
		dictVirtualDirs['tempTexto'] = dictVirtualDirs['tempTexto'] + 1
	elif tipo == 3:
		tempDir = dictVirtualDirs['tempBoleano']
		dictVirtualDirs['tempBoleano'] = dictVirtualDirs['tempBoleano'] + 1

	return tempDir

def regresaOperacion(operando):
	return {
		'+' : 0,
		'-' : 1,
		'*' : 2,
		'/' : 3,
		'%' : 4,
		'y' : 5,
		'o' : 6,
		'<' : 7,
		'>' : 8,
		'==': 9,
		'!=': 10,
		'>=': 11,
		'<=': 12,
		'=' : 13,
	}[operando]

def existenciaProc(ide):
	global cuadruplos

	exist = False
	for i in tablaProcedimientos:
		if i[0] == ide and i[1] == "global":
			exist = True
			break

	if not exist:
		print("El procedimiento '" + ide + "' no existe")
		sys.exit()

	cuadruplos.append(["era", ide, scope,"global"])

def llamadaFuncionActions(ide, scope):
	global countParameter, pTipo, pilaO, cuadruplos

	countParams = 1
	dirInicioFuncion = 0
	for i in tablaProcedimientos:
		if ide == i[0] and i[1] == scope:
			dirInicioFuncion = i[2]
			if countParameter != len(i[4]):
				print("El numero de parametros no coincide para la funcion " + ide)
				sys.exit()
			for param in i[4]:
				poptemp = pTipo.pop(len(pTipo) - countParameter)
				countParameter = countParameter - 1
				if param != poptemp:
					print("El parametro no coincide con el esperado: " + str(pilaO.pop()))
					sys.exit()
				cuadruplos.append(["param",pilaO.pop(), "", "param" + str(countParams)])
				countParams = countParams + 1
			break

	if afterDotId == "":
		cuadruplos.append(["gosub", dirInicioFuncion, "", ""])
	else:
		cuadruplos.append(["gosub", dirInicioFuncion, idAsignLlamadaFunc, scope])
	countParameter = 0

def updateVarSize(size):
	global tablaVariables, dictVirtualDirs

	tablaVariables[len(tablaVariables) - 1][4] = size
	sizeMenos1 = size - 1

	dirVirtual = 0
	if scope == "global":

		if tipoVar == "entero":
			dictVirtualDirs['globalInt'] = dictVirtualDirs['globalInt'] + sizeMenos1

		elif tipoVar == "flotante":
			dictVirtualDirs['globalFloat'] = dictVirtualDirs['globalFloat'] + sizeMenos1

		elif tipoVar == "texto":
			dictVirtualDirs['globalTexto'] = dictVirtualDirs['globalTexto'] + sizeMenos1

		elif tipoVar == "boleano":
			dictVirtualDirs['globalBoleano'] = dictVirtualDirs['globalBoleano'] + sizeMenos1
	else:
		if tipoVar == "entero":
			dictVirtualDirs['localInt'] = dictVirtualDirs['localInt'] + sizeMenos1

		elif tipoVar == "flotante":
			dirVirtual = dictVirtualDirs['localFloat']
			dictVirtualDirs['localFloat'] = dictVirtualDirs['localFloat'] + sizeMenos1

		elif tipoVar == "texto":
			dictVirtualDirs['localTexto'] = dictVirtualDirs['localTexto'] + sizeMenos1

		elif tipoVar == "boleano":
			dictVirtualDirs['localBoleano'] = dictVirtualDirs['localBoleano'] + sizeMenos1

def verificaVectorAsignacion():
	global pilaO, pTipo, cuadruplos, mapa, idAsignIsVector

	idAsignIsVector = True
	indiceTipo = pTipo.pop()
	if indiceTipo != 0:
		print("Indice no es entero")
		sys.exit()

	# cuadruplo de la verificacion
	indiceASumar = pilaO.pop()
	cuadruplos.append(["verificaBounds",indiceASumar,0,varBoundAsign])

	# cuadruplo de la abs dir
	tempBaseDir = regresaTempDirVirtual(0)
	mapa.hashMM[tempBaseDir] = dirBaseVector
	absDir = regresaTempDirVirtual(matchTipo(tipoAsignacion))

	cuadruplos.append([0,indiceASumar,tempBaseDir,absDir])
	pilaO.append(absDir)
	pTipo.append(matchTipo(tipoAsignacion))

def verificaVectorExp():
	global pilaO, pTipo, cuadruplos, mapa, varcteIdIsVector, scopeClase, varcteId

	varcteId = tempNombreVector
	varcteIdIsVector = True
	dirBaseVector = 0
	tipoAsignacion = -1
	varBoundAsign = 0

	indiceTipo = pTipo.pop()
	if indiceTipo != 0:
		print("Indice no es entero")
		sys.exit()

	exists = False;
	#checo locales
	for i in tablaVariables:
		if i[0] == varcteId and i[2] == scopeClase + scope:
			exists = True
			tipoAsignacion = i[1]
			varBoundAsign = i[4]
			dirBaseVector = i[3]
			break

	#checo globales
	if not exists:
		funcScope = "global" if scopeClase == "" else scopeClase
		for i in tablaVariables:
			if i[0] == varcteId and i[2] == funcScope:
				exists = True
				tipoAsignacion = i[1]
				varBoundAsign = i[4]
				dirBaseVector = i[3]
				break

	if not exists:
		print("La variable " + varcteId +" no ha sido declarada ")
		sys.exit()

	# cuadruplo de la verificacion
	indiceASumar = pilaO.pop()
	cuadruplos.append(["verificaBounds",indiceASumar,0,varBoundAsign])

	# cuadruplo de la abs dir
	tempBaseDir = regresaTempDirVirtual(0)
	mapa.hashMM[tempBaseDir] = dirBaseVector
	absDir = regresaTempDirVirtual(matchTipo(tipoAsignacion))

	cuadruplos.append([0,indiceASumar,tempBaseDir,absDir])
	pilaO.append(str(absDir)+"$")
	pTipo.append(matchTipo(tipoAsignacion))

# Error rule for syntax errors
def p_error(p):
	if p:
		print("line %d, Syntax error" % p.lineno)
		sys.exit()
	else:
		print("Syntax error at the end of file")



# Build the parser
parser = yacc.yacc()

# read from an external file
#fileNameToRead = input('Nombre del archivo de entrada?: ')
fr = open('prueba.in', 'r')
inputText = fr.read()

# Parsing the input
parser.parse(inputText)
